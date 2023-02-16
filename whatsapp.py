#!/usr/bin/env python3
import pywhatkit
Number = input("Enter Number Phone Have Whatsapp : ")
TimetoSentH= int(input("Enter Time to Sent Message(Hours):"))
TimetoSentM= int(input("Enter Time to Sent Message(Minutes):"))
with open('report.txt','r') as myfile:
    Massge=myfile.read()
try:
 pywhatkit.sendwhatmsg(Number,Massge,TimetoSentH,TimetoSentM)
 print("Success Sent")
except:
 print("Not Success Sent")


