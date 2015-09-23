#serialInterface - interface with the serial bus
import math
import serial

#goal position 0x1E

def rad2tich(goalPosition):
	goalPosition += math.radians(150.0)
	goalPosition = goalPosition/math.radians(300.0)
	goalPosition = goalPosition * 0x3ff
	return int(goalPosition)

def makeMessage(instruction, dataAddress, tich, ID):
	tich_l = tich & 0xff
	tich_h = (tich & 0xff00) >> 8
	message = bytearray([0xff, 0xff, ID, 5, instruction, dataAddress, tich_l, tich_h])
	return message
	
def addCheckSum(message):
	checkSum = message[2] + message[3] + message[4] + message[5] + message[6] + message[7]
	checkSum = ~checkSum & 0xFF
	message += bytearray([checkSum])
	return message

def setPosition(goalPosition, ID, dynamixel):
	tich = rad2tich(goalPosition)
	buff = makeMessage(0x03, 0x1E, tich, ID)
	buff = addCheckSum(buff)
	dynamixel.write(buff)
	#print buff
	
