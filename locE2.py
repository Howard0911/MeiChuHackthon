from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def location (source_loc, coordinate):
	source_loc[3] = 0
	x1 = coordinate[0][0]
	x2 = coordinate[1][0]
	x3 = coordinate[2][0]
	x4 = coordinate[3][0]
	
	y1 = coordinate[0][1]
	y2 = coordinate[1][1]
	y3 = coordinate[2][1]
	y4 = coordinate[3][1]
	
	z1 = coordinate[0][2]
	z2 = coordinate[1][2]
	z3 = coordinate[2][2]
	z4 = coordinate[3][2]
	
	return [coordinate[0][3] - ( (x1 - source_loc[0])**2 + (y1 - source_loc[1])**2 + (z1 - source_loc[2])**2 )**0.5,
			coordinate[1][3] - ( (x2 - source_loc[0])**2 + (y2 - source_loc[1])**2 + (z2 - source_loc[2])**2 )**0.5,
			coordinate[2][3] - ( (x3 - source_loc[0])**2 + (y3 - source_loc[1])**2 + (z3 - source_loc[2])**2 )**0.5,
			coordinate[3][3] - ( (x4 - source_loc[0])**2 + (y4 - source_loc[1])**2 + (z4 - source_loc[2])**2 )**0.5]

def error (coordinate, s_loc):
	x1 = coordinate[0][0]
	x2 = coordinate[1][0]
	x3 = coordinate[2][0]
	x4 = coordinate[3][0]
	
	y1 = coordinate[0][1]
	y2 = coordinate[1][1]
	y3 = coordinate[2][1]
	y4 = coordinate[3][1]
	
	z1 = coordinate[0][2]
	z2 = coordinate[1][2]
	z3 = coordinate[2][2]
	z4 = coordinate[3][2]
	
	dev1 = coordinate[0][3] - ( (x1 - s_loc[0])**2 + (y1 - s_loc[1])**2 + (z1 - s_loc[2])**2 )**0.5
	dev2 = coordinate[1][3] - ( (x2 - s_loc[0])**2 + (y2 - s_loc[1])**2 + (z2 - s_loc[2])**2 )**0.5
	dev3 = coordinate[2][3] - ( (x3 - s_loc[0])**2 + (y3 - s_loc[1])**2 + (z3 - s_loc[2])**2 )**0.5
	dev4 = coordinate[3][3] - ( (x4 - s_loc[0])**2 + (y4 - s_loc[1])**2 + (z4 - s_loc[2])**2 )**0.5
	
	error1 = dev1 / coordinate[0][3]
	error2 = dev2 / coordinate[1][3] 
	error3 = dev3 / coordinate[2][3]
	error4 = dev4 / coordinate[3][3]
	
	if error1 > 1E-3 or error2 > 1E-3 or error3 > 1E-3 or error4 > 1E-3:
		return 0
	else: return 1
	
#coordinate_dis = [  [x1,y1,z1,dis1]  , [...]  []   []]
coordinate_dis = [ [0,0,1,1.7] , [1,0,1,2**0.5] , [0,1,1,2**0.5] , [1,1,2,2] ]

loc = fsolve(location, [0,0,0,0], args = coordinate_dis, maxfev = 0)
#loc[3] = 'target'
if error(coordinate_dis, loc):
	print(loc[0:3])
else: print('No solution')
	