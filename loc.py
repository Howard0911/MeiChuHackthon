from scipy 
import numpy as np
import matplotlib.pyplot as plt

def location (source_loc, coordinate[4][3], distance[4])
	x1 = coordinate[0][0]
	x2 = coordinate[1][0]
	x3 = coordinate[2][0]
	x4 = coordinate[3][0]
	
	y1 = coordinate[0][1]
	y2 = coordinate[1][1]
	y3 = coordinate[2][1]
	y4 = coordinate[3][1]
	
	x1 = coordinate[0][2]
	x2 = coordinate[1][2]
	x3 = coordinate[2][2]
	x4 = coordinate[3][2]
	
	return [distance[0] - sqrt((x1 - source_loc[0])**2 + (y1 - source_loc[1])**2 + (z1 - source_loc[2])**2),
			distance[1] - sqrt((x2 - source_loc[0])**2 + (y2 - source_loc[1])**2 + (z2 - source_loc[2])**2),
			distance[2] - sqrt((x3 - source_loc[0])**2 + (y3 - source_loc[1])**2 + (z3 - source_loc[2])**2),
			distance[3] - sqrt((x4 - source_loc[0])**2 + (y4 - source_loc[1])**2 + (z4 - source_loc[2])**2)]

coordinate = [[0,0,0],[1,0,0],[0,1,0],[0,0,1]]
distance = [0.6,0.6,0.6,0.6]
loc = fsolve(location, 0, arg = coordinate, distance)
print(loc)
