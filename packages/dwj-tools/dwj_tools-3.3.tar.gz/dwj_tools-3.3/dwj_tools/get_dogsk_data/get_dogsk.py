import tcoreapi_mq as t
import warnings
import numpy as np
import datetime
import pandas as pd
import os
thisDir = os.path.dirname(__file__)
warnings.simplefilter('ignore')


print('在连接权分析')
# core = t.TCoreZMQ(quote_port="55773", trade_port="54127")
core = t.TCoreZMQ(quote_port="51864", trade_port="51834")  # UAT版本
# core = t.TCoreZMQ(quote_port="51630", trade_port="51600")  # derui版本
print('连接成功')


def get_codes_given_symbol_and_date(symbol, csd_date):
    '''获取给定symbol在给定日期下的dogsk数据
    '''
    try:
        a = core.QueryAllInstrumentInfo("Options", csd_date)
        a = pd.DataFrame(a)
    except:
        a = core.QueryAllInstrumentInfo("Options", csd_date)
        a = pd.DataFrame(a)
    b = a['Instruments']['Node']
    if symbol=='159915':
        c = pd.DataFrame(b[1])
    else:
        c = pd.DataFrame(b[0])
    if symbol=='510050':
        code_list = c.iloc[0, -1]
    elif symbol=='510300':
        code_list = c.iloc[1, -1]
    elif symbol=='510500':
        code_list = c.iloc[2, -1]
    elif symbol=='159915':
        code_list = c.iloc[0, -1]
    interval='DOGSK'
    len_of_df = 0
    start_str = '00'
    end_str = '07'
    for month in [0, 1, 2, 3]:
        print(f'当前month {month}')
        tau = int(code_list['Node'][2+month]['Node'][0]['TradeingDays'][0])
        for j, crt_symbol in enumerate(code_list['Node'][2+month]['Node'][0]['Contracts']):
            new_option_data = pd.DataFrame(core.SubHistory(
                crt_symbol, interval, csd_date+start_str, csd_date+end_str))
            temp_date = len(new_option_data) * [csd_date]
            flag = len(new_option_data) * ['C']
            new_option_data['date'] = temp_date
            new_option_data['flag'] = flag
            new_option_data['tau'] = tau
            if j == 0 and month == 0:
                df = new_option_data
                len_of_df = len(df)
            else:
                df = df.append(new_option_data.iloc[:len_of_df,:])
        for k in code_list['Node'][2+month]['Node'][1]['Contracts']:
            new_option_data = pd.DataFrame(core.SubHistory(
                k, interval, csd_date+start_str, csd_date+end_str))
            temp_date = len(new_option_data) * [csd_date]
            flag = len(new_option_data) * ['P']
            new_option_data['date'] = temp_date
            new_option_data['flag'] = flag
            new_option_data['tau'] = tau
            df = df.append(new_option_data.iloc[:len_of_df,:])
    final_df = pd.DataFrame()
    final_df['symbol'] = df['Symbol']
    final_df['datetime'] = df['DateTime']
    close = np.array(pd.to_numeric(df['p']))
    final_df['close'] = close
    iv = np.array(pd.to_numeric(df['iv']))
    final_df['iv'] = iv
    delta = np.array(pd.to_numeric(df['de']))/100
    final_df['delta'] = delta
    vega = np.array(pd.to_numeric(df['ve']))
    final_df['vega'] = vega
    theta = np.array(pd.to_numeric(df['th']))
    final_df['theta'] = theta
    gamma = np.array(pd.to_numeric(df['ga']))
    final_df['gamma'] = gamma
    charm = np.array(pd.to_numeric(df['ch']))
    final_df['charm'] = charm
    vanna = np.array(pd.to_numeric(df['va']))
    final_df['vanna'] = vanna
    vomma = np.array(pd.to_numeric(df['vo']))
    final_df['vomma'] = vomma
    speed = np.array(pd.to_numeric(df['spe']))
    final_df['speed'] = speed
    zomma = np.array(pd.to_numeric(df['zo']))
    final_df['zomma'] = zomma
    final_df['date'] = df['date']
    final_df['flag'] = df['flag']
    final_df['tau'] = df['tau']
    return final_df


def get_synf_dogsk(symbol, crt_date):
    '''获取给定symbol在给定日期下合成期货dogsk数据
    '''
    try:
        a = core.QueryAllInstrumentInfo("Options", crt_date)
        a = pd.DataFrame(a)
    except:
        a = core.QueryAllInstrumentInfo("Options", crt_date)
        a = pd.DataFrame(a)
    b = a['Instruments']['Node']
    if symbol=='159915':
        c = pd.DataFrame(b[1])
    else:
        c = pd.DataFrame(b[0])
    if symbol=='510050':
        code_list = c.iloc[0, -1]
        symbol_str = 'TC.F.U_SSE.510050.'
    elif symbol=='510300':
        code_list = c.iloc[1, -1]
        symbol_str = 'TC.F.U_SSE.510300.'
    elif symbol=='510500':
        code_list = c.iloc[2, -1]
        symbol_str = 'TC.F.U_SSE.510500.'
    elif symbol=='159915':
        code_list = c.iloc[0, -1]
        symbol_str = 'TC.F.U_SZSE.159915.'
    temp_df = pd.DataFrame()
    for j in range(4):
        print(j)
        csd_month = code_list['Node'][j+2]['CHS']
        tau = int(code_list['Node'][2+j]['Node'][0]['TradeingDays'][0])
        syn_f = core.SubHistory(symbol_str+csd_month, 'DOGSK', crt_date+'00', crt_date+'07')
        while len(syn_f)<3:
            syn_f = core.SubHistory(symbol_str+csd_month, 'DOGSK', crt_date+'00', crt_date+'07')
        syn_f = pd.DataFrame(syn_f)
        temp_df[f'cskew_{j}'] = pd.to_numeric(syn_f['cskew'])
        temp_df[f'pskew_{j}'] = pd.to_numeric(syn_f['pskew'])
        temp_df[f'tau_{j}'] = len(syn_f) * [tau]
        temp_df[f'iv_{j}'] = pd.to_numeric(syn_f['iv'])
        temp_df[f'close_{j}'] = pd.to_numeric(syn_f['p'])
        temp_df[f'civ25_{j}'] = pd.to_numeric(syn_f['dciv25'])
        temp_df[f'piv25_{j}'] = pd.to_numeric(syn_f['dpiv25'])
        temp_df[f'civ10_{j}'] = pd.to_numeric(syn_f['dciv10'])
        temp_df[f'piv10_{j}'] = pd.to_numeric(syn_f['dpiv10'])
    temp_df['date'] = [crt_date] * len(temp_df)
    temp_df.index = syn_f['DateTime']
    return temp_df


def get_und_dogsk(symbol, crt_date):
    '''获取给定symbol在给定日期下标的dogsk数据
    '''
    if symbol=='510050':
        symbol_str = 'TC.S.SSE.510050'
    elif symbol=='510300':
        symbol_str = 'TC.S.SSE.510300'
    elif symbol=='510500':
        symbol_str = 'TC.S.SSE.510500.'
    elif symbol=='159915':
        symbol_str = 'TC.S.SZSE.159915.'
    und = core.SubHistory(symbol_str, '1K', crt_date+'00', crt_date+'07')
    while len(und)<3:
        und = core.SubHistory(symbol_str, '1K', crt_date+'00', crt_date+'07')
    und = pd.DataFrame(und)
    temp_und = pd.DataFrame()
    temp_und['date'] = und['Date']
    temp_und['datetime'] = und['DateTime']
    temp_und['close'] = pd.to_numeric(und['Close'])
    temp_und['open'] = pd.to_numeric(und['Open'])
    temp_und['high'] = pd.to_numeric(und['High'])
    temp_und['low'] = pd.to_numeric(und['Low'])
    temp_und['volume'] = pd.to_numeric(und['Volume'])
    return temp_und


def update():
    tradingday = pd.read_excel(thisDir+'\\tradingday.xlsx')
    crtdate = datetime.date.today()
    crtdate = datetime.datetime(crtdate.year, crtdate.month, crtdate.day, 00, 00)
    iid = tradingday.loc[tradingday.date < crtdate].index.tolist()[-1]  # 前一个交易日的index
    date = list(tradingday['date'])[:iid+1]
    date_str_list = [i.strftime('%Y%m%d') for i in date]
    start_idx_510050 = 1219  # 权分析暂时为2022-01-02开始
    start_idx_510300 = 1219
    start_idx_510500 = 1877  # 创业板与500etf均为2022-09-19
    start_idx_159915 = 1877
    symbol_list = ['510050', '510300', '510500', '159915']
    dogsk_synf = pd.HDFStore(thisDir+'\\dogsk_synf.h5')
    synf_keys = dogsk_synf.keys()
    dogsk_synf.close()
    print(len(date_str_list))
    for csd_symbol in symbol_list:
        days_of_key_of_symbol = []
        for csd_key in synf_keys:
            if csd_symbol in csd_key:
                days_of_key_of_symbol += [int(csd_key[-8:])]
        if len(days_of_key_of_symbol)==0:
            temp_start_idx = locals()[f'start_idx_{csd_symbol}']
            print(f'已有的hdf中没有{csd_symbol}对应的合成期货, 从头开始取')
        else:
            temp_start_idx = date_str_list.index(str(max(days_of_key_of_symbol))) + 1
            if temp_start_idx==len(date_str_list):
                print(f'{csd_symbol}合成期货已经是最新数据, 进行下一品种')
                continue
            print(f'{csd_symbol}已有的合成期货数据截止到{date_str_list[temp_start_idx-1]}, 新数据从{date_str_list[temp_start_idx]}开始取')
        csd_date_list = date_str_list[temp_start_idx:]
        for i, crt_date in enumerate(csd_date_list):
            print(f'当前获取{crt_date}')
            df = get_synf_dogsk(csd_symbol, crt_date)
            if len(df)>1:
                df.to_hdf(thisDir+'\\dogsk_synf.h5', key=csd_symbol+crt_date)

    dogsk_und = pd.HDFStore(thisDir+'\\dogsk_und.h5')
    und_keys = dogsk_und.keys()
    dogsk_und.close()
    for csd_symbol in symbol_list:
        days_of_key_of_symbol = []
        for csd_key in und_keys:
            if csd_symbol in csd_key:
                days_of_key_of_symbol += [int(csd_key[-8:])]
        if len(days_of_key_of_symbol)==0:
            temp_start_idx = locals()[f'start_idx_{csd_symbol}']
            print(f'已有的hdf中没有{csd_symbol}对应的标的, 从头开始取')
        else:
            temp_start_idx = date_str_list.index(str(max(days_of_key_of_symbol))) + 1
            if temp_start_idx==len(date_str_list):
                print(f'{csd_symbol}标的已经是最新数据, 进行下一品种')
                continue
            print(f'{csd_symbol}已有的标的数据截止到{date_str_list[temp_start_idx-1]}, 新数据从{date_str_list[temp_start_idx]}开始取')
        csd_date_list = date_str_list[temp_start_idx:]
        for i, crt_date in enumerate(csd_date_list):
            print(f'当前获取{crt_date}')
            df = get_und_dogsk(csd_symbol, crt_date)
            if len(df)>1:
                df.to_hdf(thisDir+'\\dogsk_und.h5', key=csd_symbol+crt_date)

    dogsk_option = pd.HDFStore(thisDir+'\\dogsk_option.h5')
    option_keys = dogsk_option.keys()
    dogsk_option.close()
    for csd_symbol in symbol_list:
        print(csd_symbol)
        days_of_key_of_symbol = []
        for csd_key in option_keys:
            if csd_symbol in csd_key:
                days_of_key_of_symbol += [int(csd_key[-8:])]
        if len(days_of_key_of_symbol)==0:
            temp_start_idx = locals()[f'start_idx_{csd_symbol}']
            print(f'已有的hdf中没有{csd_symbol}对应的期权数据, 从头开始取')
        else:
            temp_start_idx = date_str_list.index(str(max(days_of_key_of_symbol))) + 1
            if temp_start_idx==len(date_str_list):
                print(f'{csd_symbol}期权已经是最新数据, 进行下一品种')
                continue
            print(f'{csd_symbol}已有的期权数据截止到{date_str_list[temp_start_idx-1]}, 新数据从{date_str_list[temp_start_idx]}开始取')
        csd_date_list = date_str_list[temp_start_idx:]
        for i, crt_date in enumerate(csd_date_list):
            print(f'当前获取{crt_date}')
            df = get_codes_given_symbol_and_date(csd_symbol, crt_date)
            if len(df)>1:
                df.to_hdf(thisDir+'\\dogsk_option.h5', key=csd_symbol+crt_date)


if __name__ == '__main__':
    update()

