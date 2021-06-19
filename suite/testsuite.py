import unittest
import time
import os
import sys
sys.path.append('.')
from util.log import LogMessage
from util import BSTestRunner
from config.config import description, reporttitle

path = os.getcwd()
case_path = os.path.join(path,'case')
log = LogMessage()

def create_report():
    log.info_log('Start to create report:')
    test_suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*test.py', top_level_dir=None)
    # breakpoint()
    for tests in discover:
        for test in tests:
            log.info_log(message=f'Imported: {test}')
            test_suite.addTest(test)
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    report_dir = os.path.join(path, 'report',f'{now}.html')
    re_open = open(report_dir, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title=reporttitle, description=description)
    runner.run(test_suite)

