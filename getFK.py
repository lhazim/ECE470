import numpy as np
import math

#getFK - forward kinematics
#theta is an array

#theta = np.matrix([0, 0, 0])

def getFK(theta): 
	l1 = 0.3
	l2 = 0.2
	l3 = 0.1
	x = l1*math.cos(theta.item(0)) + l2*math.cos(theta.item(0) + theta.item(1)) + l3*math.cos(theta.item(0) + theta.item(1) + theta.item(2))
	y = l1*math.sin(theta.item(0)) + l2*math.sin(theta.item(0) + theta.item(1)) + l3*math.sin(theta.item(0) + theta.item(1) + theta.item(2))
	#print np.matrix([x, y])
	return np.matrix([x, y])

#getFK(theta)

