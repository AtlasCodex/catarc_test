import io
import os
import sys

from ddt.excel_ddt import ddt

if __name__ == '__main__':
    os.system('rd /s/q result')
    os.system('rd /s/q report')

    ddt.run_web_case('./lib/cases/测试用例.xlsx')
    os.system('allure generate result -o report --clean')
