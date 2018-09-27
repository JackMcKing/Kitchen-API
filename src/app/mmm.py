import os, sys

os.chdir('C:\\Users\\chenguwa\\PycharmProjects\\KitchenAPI\\src')
sys.path.append('C:\\Users\\chenguwa\\PycharmProjects\\KitchenAPI\\src')

from sql_handler.SQL_handler import SQL_handler

s = SQL_handler(path='C:\\Users\\chenguwa\\PycharmProjects\\KitchenAPI\\src\\resource\\links.sql')
s.readdata()