#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_hdf.py
@Time    :   2022/01/15 15:46:05
@Author  :   DingWenjie
@Contact :   359582058@qq.com
@Desc    :   None
'''

import pandas as pd
import os
import datetime

pt = os.path.dirname(os.path.realpath(__file__))
files = {
        'A': os.path.join(pt, 'get_data_from_wind/option_50_data_wind.h5'),
        'B': os.path.join(pt, 'get_data_from_wind/etf_50_data_wind.h5'),
        'C': os.path.join(pt, 'get_data_from_qfx/option_data_50.h5'),
        'D': os.path.join(pt, 'get_data_from_qfx/option_data_300.h5'),
        'E': os.path.join(pt, 'get_data_from_qfx/etf_50.h5'),
        'F': os.path.join(pt, 'get_data_from_qfx/etf_300.h5'),
        'G': os.path.join(pt, 'get_dogsk_data/dogsk_option.h5'),
        'H': os.path.join(pt, 'get_dogsk_data/dogsk_und.h5'),
        'I': os.path.join(pt, 'get_dogsk_data/dogsk_synf.h5'),
        'J': os.path.join(pt, 'get_dogsk_data/tradingday.xlsx')
}


def read_data_wind():
    option_data = pd.read_hdf(files['A'])
    etf_data = pd.read_hdf(files['B'])
    return option_data, etf_data


def read_data_qfx_300():
    option_data = pd.read_hdf(files['D'])
    etf_data = pd.read_hdf(files['F'])
    return option_data, etf_data


def read_data_qfx_50():
    option_data = pd.read_hdf(files['C'])
    etf_data = pd.read_hdf(files['E'])
    return option_data, etf_data


def read_data_dogsk(symbol, date, min_range='all'):
    option_data = pd.read_hdf(files['G'], key=symbol+date)
    und_data = pd.read_hdf(files['H'], key=symbol+date)
    synf_data = pd.read_hdf(files['I'], key=symbol+date)
    if min_range=='all':
        return option_data, und_data, synf_data
    csd_range = []
    for i in range(int(len(option_data)/240)):
        for csd_id in min_range:
            csd_range += [i*240+csd_id]
    temp_option = option_data.iloc[csd_range, :]
    temp_und = und_data.iloc[min_range, :]
    temp_synf = synf_data.iloc[min_range, :]
    return temp_option, temp_und, temp_synf


def get_und_and_synf_given_range(symbol, start_date=None, end_date=None, csd_range='all'):
    tradingday = pd.read_excel(files['J'])
    crtdate = datetime.date.today()
    crtdate = datetime.datetime(crtdate.year, crtdate.month, crtdate.day, 00, 00)
    iid = tradingday.loc[tradingday.date < crtdate].index.tolist()[-1]  # 前一个交易日的index
    date = list(tradingday['date'])[:iid+1]
    date_str_list = [i.strftime('%Y%m%d') for i in date]
    start_idx_510050 = 1219  # 权分析暂时为2022-01-02开始
    start_idx_510300 = 1219
    start_idx_510500 = 1877  # 创业板与500etf均为2022-09-19
    start_idx_159915 = 1877
    if start_date:
        start_idx = max(date_str_list.index(start_date), locals()[f'start_idx_{symbol}'])
    if end_date:
        end_idx = min(iid, date_str_list.index(end_date))
    date_list = date_str_list[start_idx:end_idx+1]
    und = pd.DataFrame()
    synf = pd.DataFrame()
    for csd_date in date_list:
        _, temp_und, temp_synf = read_data_dogsk(symbol, csd_date, csd_range)
        und = und.append(temp_und)
        synf = synf.append(temp_synf)
    return und, synf


if __name__ == '__main__':
    pass