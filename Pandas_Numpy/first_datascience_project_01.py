import pandas as pd
import numpy as np
import csv
#Open csv file up
with open ('t187ap03_L.csv') as file:
    file_01 = csv.reader(file)
    for row in file_01:
        print(row)
#read the csv file
park_1 = pd.read_csv('t187ap03_L.csv')
#find the headers you want to shown 
park_1['公司名稱']
company_name = park_1.公司名稱
park_1['住址']
address=park_1.住址
park_1['上市日期']
listing_date=park_1.上市日期
park_1['實收資本額']
Paid_in_capital = park_1.實收資本額
#Print any types of data in csv file
print('公司名稱',company_name)
print('公司住址',address)
print('上市日期',listing_date)
print('實收資本額',Paid_in_capital)

#to add those city up
#add those data to SQL
#Using those data and show it on Tkinter
