from peoples import people
from finance import salary
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

'''
хотя в нашем случае допустимо
from people import *
from salary import *
'''

if __name__ == '__main__':
    print(datetime.now())
    people.get_employees()
    salary.calculate_salary()