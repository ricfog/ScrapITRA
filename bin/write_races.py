from ..src import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start_date', type=str, default="01/01/2010", help='initial date')
parser.add_argument('--end_date', default="01/01/2011", type=str, help='end date')
parser.add_argument('--path', default="race", type=str, help='path')
args = parser.parse_args()


browser = get_browser('https://itra.run/community/', False)

try:
   from login_credentials import *
   login(username, password, browser)
except ImportError:
    pass

races_info = get_races(browser, args.start_date, args.end_date, args.path)
