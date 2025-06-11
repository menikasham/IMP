from people import get_employees
from salary import calculate_salary
from datetime import datetime
import pandas as pd

'''
хотя в нашем случае допустимо
from people import *
from salary import *
'''

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    calculate_salary()