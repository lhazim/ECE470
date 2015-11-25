#matrices.py: get matrix functions

from joints import * #LSP, LSR, LSY, LEP, LWY, LWR, LE
import numpy as np
import math

#T = transformation matrix, 4x4
#R = rotational matrix, 3x3
#P = translation matrix, 3x1

getT(R,P):
	T = R + P + [0, 0, 0, 1]
	return T 

getR(theta): 
	Rx = np.matrix[1, 0, 0, 0, cos(theta(0)), -sin(theta(0)), 0, sin(theta(0)), cos(theta(0))]
	Ry = np.matrix[cos(theta(1)), 0, sin(theta(1)), 0, 1, 0, -sin(theta(1)), 0, cos(theta(1))]
	Rz = np.matrix[cos(theta(2)), -sin(theta(2)), 0, sin(theta(2)), -cos(theta(2)), 0, 0, 0, 1]
	R = Rx*Ry*Rz
	return R

getP(Kin, i): 
	
getTheta(R): 
	thetax = arctan(R(2,1)/R(2,2))
	thetay = arctan(R(1,0)/R(0,0))
	thetaz = arctan(-R(2,0)/(R(2,1)^2 + R(2,2)^2)
	return [thetax, thetay, thetaz]
