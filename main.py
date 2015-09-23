#main.py - main process
from sinInput import*
import ID
import serial
from time import time
from serialInterface import *

actuatorID = ID.getID()
freq = input('Enter desired frequency: ')
amp = input('Enter desired amplitude: ') 
numPeriods = input('Enter the number of periods you would like: ')
x = 1
period = 1/freq
startTime = time() 
dynamixel = serial.Serial('/dev/ttyUSB0', 1000000) 
while (x == 1):
	setPosition(sinusoidalInput(freq, amp), actuatorID, dynamixel)
	#print rad2tich(sinusoidalInput(freq, amp)) 
	if ((time() - startTime) >= numPeriods*period):
		x = 0
dynamixel.close()
