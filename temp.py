#1 blpapi
pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
import blpapi


# 1 xbbg
pip install xbbg
from xbbg import blp

blp.bdp(tickers='NVDA US Equity', flds=['Security_Name', 'PX_LAST', 'GICS_Sector_Name'])
blp.bdh(tickers='NVDA US Equity', flds=['PX_LAST'], start_date='2018-10-10', end_date='2018-10-20')

# 3 other options?




