#!/usr/bin/env python3
from datetime import datetime
now = datetime.now()
dt_stw = now.strftime("%H:%M:%S")
dt_std = now.strftime("%d/%m/%Y")
Date = dt_std+';'+dt_stw
yourname = input("Enter Your Name :")
report = input("Enter Report :")
thanks = input("Enter your Manager :")
yourcompany = input("Enter Your Company :")
with open('report.txt','a') as myfile:
    myfile.write(yourcompany+' Company')
with open('report.txt','a') as myfile:
    myfile.write('\nDate: '+Date)
with open('report.txt','a') as myfile:
    myfile.write('\nFrom :Eng.'+yourname)    
with open('report.txt','a') as myfile:
    myfile.write('\nTo: Mr.'+thanks)
with open('report.txt','a') as myfile:
    myfile.write('\nHello')
with open('report.txt','a') as myfile:
    myfile.write('\n  ')
with open('report.txt','a') as myfile:
    myfile.write('\nReport:'+report)
with open('report.txt','a') as myfile:
    myfile.write('\n  ')
with open('report.txt','a') as myfile:
    myfile.write('\n  ')
with open('report.txt','a') as myfile:
    myfile.write('\nThanks for Reading')
with open('report.txt','a') as myfile:
    myfile.write('\nProgrammer By Eng.MahammadQassem')
