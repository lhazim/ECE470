#jacobian.py - jacobian function

import numpy as np
import math
from getFK import getFK

J = np.zeros((2, 3))
#theta = np.array([math.pi,math.pi*0.25,math.pi*0.5])
#ddtheta = (2*math.pi)/1000

def getJ(ddtheta, theta): 
	e = getFK(theta)
	for i in range(0,2):
		newTheta = theta
		for j in range(0,3):
			newTheta[j] = newTheta[j] + ddtheta
			deltaE = getFK(newTheta) - e
			J[i,j] = deltaE.item(i)/ddtheta
			#print J
	return J

#getJ(ddtheta, theta)
