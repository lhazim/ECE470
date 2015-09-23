#sinInput.py - generates and sends input

from time import time
from math import *

def sinusoidalInput(freq, amp):
	currentTime = time()
	goalPosition = amp*sin(2*pi*freq*currentTime);
	#print(goalPosition);   
	return radians(goalPosition)
	


