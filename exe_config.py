import os
import sys
from playwright._impl._driver import compute_driver_executable


def exe_bin_loader():
    if getattr(sys, 'frozen', False):
        os.environ['PLAYWRIGHT_BROWSERS_PATH'] = os.path.join(sys._MEIPASS, 'playwright')
    else:
        os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '0'

