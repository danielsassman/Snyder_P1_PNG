#get height of grid
def get_height(grid):
	return (len(grid))

#get width of grid
def get_width(grid):
	return (len(grid[0]))

	
#calculate energy
def energy_at(grid,r,c):
	return (width_energy(grid, r, c) + height_energy(grid,r,c))

def energy(grid):
	newGrid = [[0 for x in range(get_width(grid))]for x in range(get_height(grid))]
	for i in range(get_height(grid)):
		for j in range (get_width(grid)):
			newGrid[i][j] = energy_at(grid, i , j)
	return newGrid

def get_red(grid, r, c):
	return((grid[r][c])[0])

def get_green(grid, r, c):
	return((grid[r][c])[1])

def get_blue(grid, r, c):
	return((grid[r][c])[2])

#calculate width energy
def width_energy(grid, r, c):
	if(c==0):
		red = (get_red(grid, r, (get_width(grid)-1)) - get_red(grid, r, (c+1)))
		green = (get_green(grid, r, (get_width(grid)-1)) - get_green(grid, r, (c+1)))
		blue = (get_blue(grid, r, (get_width(grid)-1)) - get_blue(grid, r, (c+1)))

	elif(c==get_width(grid)-1):
		red = (get_red(grid, r, (c-1)) - get_red(grid, r, 0))
		green = (get_green(grid, r, (c-1)) - get_green(grid, r, 0))
		blue = (get_blue(grid, r, (c-1)) - get_blue(grid, r, 0))

	else:
		red = (get_red(grid, r, (c-1)) - get_red(grid, r, (c+1)))
		green = (get_green(grid, r, (c-1)) - get_green(grid, r, (c+1)))
		blue = (get_blue(grid, r, (c-1)) - get_blue(grid, r, (c+1)))
	return ((red * red) + (green * green) + (blue * blue))


#calculate height energy
def height_energy(grid, r, c):
	if(r==0):
		red = (get_red(grid, (get_height(grid)-1), c) - get_red(grid, (r+1), c))
		green = (get_green(grid, (get_height(grid)-1), c) - get_green(grid, (r+1), c))
		blue = (get_blue(grid, (get_height(grid)-1), c) - get_blue(grid, (r+1), c))
	if(r==get_height(grid)-1):
		red = (get_red(grid, (r-1), c) - get_red(grid, 0, c))
		green = (get_green(grid, (r-1), c) - get_green(grid, 0, c))
		blue = (get_blue(grid, (r-1), c) - get_blue(grid, 0, c))
	else:
		red = (get_red(grid, (r-1), c) - get_red(grid, (r+1), c))
		green = (get_green(grid, (r-1), c) - get_green(grid, (r+1), c))
		blue = (get_blue(grid, (r-1), c) - get_blue(grid, (r+1), c))
	return ((red * red) + (green * green) + (blue * blue))

#HELPER FUNCTIONS

#retrieves element at r,c
def ret_element(grid,r,c):
	print(grid[r][c])


#FINDING PATHS
def find_vertical_path(grid):
	vertCoords = [(0,0) for x in range(get_height(grid))]
	vertGrid = energy(grid)
	lowest = vertGrid[0][0]
	k = 1
	c = 0 #setting column number
	for i in range (get_width(grid)-1): #finding lowest in top row
		if(vertGrid[0][i]) < lowest:
			lowest = vertGrid[0][i]
			vertCoords[0] = (0,i)
			c = i
	while k < (get_height(grid)): #moving down the grid
		nextCoord = vertGrid[k][c]
		if c > 0 and vertGrid[k][c-1] < nextCoord:
			c = c-1
			pass
		elif c < (get_width(grid)-1) and vertGrid[k][c+1] < nextCoord:
			c = c+1
		vertCoords[k] = (k,c)
		k = k + 1			 
	return vertCoords


def find_horizontal_path(grid):
	horCoords = [(0,0) for x in range(get_width(grid))]
	horGrid = energy(grid)
	lowest = horGrid[0][0]
	k = 1
	r = 0 #setting row number
	for i in range (get_height(grid)-1): #finding lowest in top row
		if(horGrid[i][0]) < lowest:
			lowest = horGrid[i][0]
			horCoords[0] = (i,0)
			r = i
	while k < (get_width(grid)): #moving across the grid
		nextCoord = horGrid[r][k]
		if r > 0 and horGrid[r-1][k] < nextCoord:
			r = r-1
			pass
		elif r < (get_height(grid)-1) and horGrid[r+1][k] < nextCoord:
			r = r+1
		horCoords[k] = (r,k)
		k = k + 1			 
	return horCoords

def remove_vertical_path(grid, path):
	for i in range (get_height(grid)):
		del grid[(path[i][0])][(path[i][1])]
	return grid


def remove_horizontal_path(grid, path):
	height = get_height(grid)
	width = get_width(grid)
	for i in range (get_width(grid)):
		grid[(path[i][0])][(path[i][1])] = (-1,i,-1)
	grid = list(map(list,zip(*grid))) #transposing grid
	for k in range (get_height(grid)):
		del grid[(path[k][1])][(path[k][0])]
	grid = list(map(list,zip(*grid))) #returning grid to normal state
	return grid

def read_lines(filename):
	k=-1
	com = 0
	y = 0
	with open(filename, 'r') as ppm:
		data = ppm.readlines()
		k += 1
		if(data[k][0] == '#'):
			com +=1	
	newLen = len(data)-com
	data2 = [0 for x in range(len(data))]
	for r in range(newLen):
		if(data[r][0] != "#"):
			data2[r-y] = data[r]
		else:
			y += 1
	#print(len(data2[0]))
	#print(data2[1])
	#print(data2[2])
	#print(data2[3])
	#print(data2[4])
	#print(data2[len(data2)-2])
	#print(data2[len(data2)-1])
	return data2

def ppm_to_grid(filename):
	data = read_lines(filename)
	rgbstring = ""
	rowcol = data[1].split()
	row = rowcol[0]
	col = rowcol[1]
	print("type = " + data[0])
	print("row = " + row)
	print("col = " + col)
	print("max length = " + data[2])
	print("data length = " + str(len(data)))
	for k in range(3,len(data)):
		rgbstring += str(data[k])
	data2 = rgbstring.split()
	#print(data2)
	print("data2 " + str(len(data2)))
	rgblength = int(row) * int(col)
	print("rgb length = " + str(rgblength))
	datacount = -1
	

	rgbcoords = [(0,0,0) for x in range(rgblength)]
	for k in range(rgblength):
		datacount += 1
		num1 = data2[datacount]
		datacount += 1
		num2 = data2[datacount]
		datacount += 1
		num3 = data2[datacount]
		rgbcoords[k] = (num1, num2, num3)
	print("rgbcoords length = " + str(len(rgbcoords)))
	
	#HAVE TO SEPERATE BY ROWS. PUTTING EACH ROW INTO A INDEX OF A 2D LIST
	finalMatrix = [[0 for x in range(int(col))] for x in range(int(row))]
	print("final matrix length = " + str(len(finalMatrix)))
	print("final matrix2 length = " + str(len(finalMatrix[0])))
	print("rgbcoords[0] = " + str(rgbcoords[0]))
	colCount = 0
	rowCount = 0
	
	for h in range(len(rgbcoords)-1):
		
		finalMatrix[rowCount][colCount] = rgbcoords[h]
		#print("finalmatrix: " + str(finalMatrix[rowCount][colCount]));
		#print(h)
		print("h = " + str(h) + " row = " + str(rowCount) + " col = " + str(colCount))
		#print(colCount)
		colCount += 1
		if(colCount==(int(col))):
			rowCount += 1
			colCount = 0
	print("rgbcoords = " + str(len(rgbcoords)))
	print("finalmatrix[0] = " + str(finalMatrix[0]))
	print("length finalmatrix[0] = " + str(len(finalMatrix[0])))
	print("finalmatrix[10] = " + str(finalMatrix[10]))
	#return finalMatrix		
	#return rgbcoords
	#print(rgbcoords[0])
	#print(rgbcoords[1])
	#print(rgbcoords[tupleCount-1])
	

def main():

	
	p1 = [
      [(100, 75,200), (100,100,200), (100,100,200), (100,100,200), (200,125,200)],
      [(150, 30,180), (150, 50,180), (100,120,180), (100,120,180), (100,120,180)],
      [(100, 75,100), (100, 80,100), (100, 85,100), (100, 95,100), (100,110,100)],
      [(200,100, 10), (200,100, 10), (200,100, 10), (210,200, 10), (255,  0, 10)]
     ]
	path = find_horizontal_path(p1)
	print(path)
	print(p1)
	print()
	p1 = remove_horizontal_path(p1,path)
	print(p1)
