'''
读取数据:
import dwj_tools.read_hdf as r
option,etf = r.read_data_wind()  # wind数据
option,etf = r.read_data_qfx_300()  # 权分析300
option,etf = r.read_data_qfx_50()  # 权分析50
option, und, synf = r.read_data_dogsk(symbol, date, min_range='all')  # dogsk数据
und, synf = r.get_und_and_synf_given_range(symbol, start_date=None, end_date=None, csd_range='all')  # 给定时间范围获取dogsk标的与合成期货数据

更新数据:
from dwj_tools.get_data_from_wind import update_option_data_wind as u  # wind更新
from dwj_tools.get_data_from_qfx import update_data_qfx as u  # 权分析更新
from dwj_tools.get_dogsk_data import get_dogsk as u
u.update()
'''