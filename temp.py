conda install ruamel.yaml
conda install pyarrow

import time
import datetime
import pandas as pd

#pdblp wrapper for blpapi
pip install pdblp

python -m pip install git+https://github.com/kyuni22/pybbg
import pybbg as pybbg
bbg = pybbg.Pybbg()
bbg.bdh('EUR Curncy', 'PX_LAST', '20200525')


#xbbg
pip install xbbg
from xbbg import blp

blp.bdib('AAPL US Equity', 'PX_LAST', '2022-05-24')
blp.bdp(tickers='NVDA US Equity', flds=['Security_Name', 'PX_LAST', 'GICS_Sector_Name'])
blp.bdh(tickers='NVDA US Equity', flds=['PX_LAST'], start_date='2018-10-10', end_date='2018-10-20')


#blpapi
pip install --index-url=https://bcms.bloomberg.com/pip/simple blpapi
import blpapi



