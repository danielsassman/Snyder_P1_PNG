#get height of grid
def height(grid):
	return (len(grid))

#get width of grid
def width(grid):
	return (len(grid[0]))

	
#calculate energy
def energy_at(grid,r,c):
	return (width_energy(grid, r, c) + height_energy(grid,r,c))

def energy(grid):
	newGrid = [[0 for x in range(width(grid))]for x in range(height(grid))]
	for i in range(height(grid)):
		for j in range (width(grid)):
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
		red = (get_red(grid, r, (width(grid)-1)) - get_red(grid, r, (c+1)))
		green = (get_green(grid, r, (width(grid)-1)) - get_green(grid, r, (c+1)))
		blue = (get_blue(grid, r, (width(grid)-1)) - get_blue(grid, r, (c+1)))

	elif(c==width(grid)-1):
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
		red = (get_red(grid, (height(grid)-1), c) - get_red(grid, (r+1), c))
		green = (get_green(grid, (height(grid)-1), c) - get_green(grid, (r+1), c))
		blue = (get_blue(grid, (height(grid)-1), c) - get_blue(grid, (r+1), c))
	if(r==height(grid)-1):
		red = (get_red(grid, (r-1), c) - get_red(grid, 0, c))
		green = (get_green(grid, (r-1), c) - get_green(grid, 0, c))
		blue = (get_blue(grid, (r-1), c) - get_blue(grid, 0, c))
	else:
		red = (get_red(grid, (r-1), c) - get_red(grid, (r+1), c))
		green = (get_green(grid, (r-1), c) - get_green(grid, (r+1), c))
		blue = (get_blue(grid, (r-1), c) - get_blue(grid, (r+1), c))
	return ((red * red) + (green * green) + (blue * blue))


#retrieves element at r,c
def ret_element(grid,r,c):
	print(grid[r][c])



def find_vertical_path(grid):
	vertCoords = [(0,0) for x in range(height(grid))]
	totals = [0 for x in range(width(grid))]
	totalCount = 0
	vertGrid = energy(grid)
	totalEnergy = 0
	lowest = vertGrid[0][0]
	k = 1
	totalReturn = 0
	up = 0
	r = 0 #setting row number
	
	#testing each starting point
	for h in range (width(grid)):
		r = h
		vertCoords[0] = (0,h)
		for k in range (1,height(grid)): #moving across the grid
			nextCoord = vertGrid[k][r]
			if r > 0 and vertGrid[k][r-1] <= nextCoord:
				if r < (width(grid)-1) and vertGrid[k][r+1] < vertGrid[k][r-1]:
					r = r + 1
					up = 1
				else:
					r = r-1
			elif r < (width(grid)-1) and  vertGrid[k][r+1] < nextCoord and up < 1:
				r = r+1
			up = 0
			vertCoords[k] = (k,r)
			k = k + 1
		#returning a value for each starting point and storing in totals array
		for l in range(height(grid)):
			totalEnergy = totalEnergy + int(energy_at(grid, int(vertCoords[l][0]), int(vertCoords[l][1])))
		totals[totalCount] = totalEnergy
		totalCount = totalCount + 1
		totalEnergy = 0
		vertCoords = [(0,0) for x in range(height(grid))]
	minValue = totals[0]
	for p in range (width(grid)):
		if(totals[p] < minValue):
			totalReturn = p
			minValue = totals[p]
	vertCoords[0] = (0, totalReturn)
	r = totalReturn
	#starting at the correct point and returning the array that will be deleted
	for k in range (1,height(grid)): #moving across the grid
		nextCoord = vertGrid[k][r]
		if r > 0 and vertGrid[k][r-1] <= nextCoord:
			if r < (width(grid)-1) and vertGrid[k][r+1] < vertGrid[k][r-1]:
				r = r + 1
				up = 1
			else:
				r = r-1
		elif r < (width(grid)-1) and vertGrid[k][r+1] < nextCoord and up < 1:
			r = r+1
		up = 0
		vertCoords[k] = (k,r)
		k = k + 1
		
	return vertCoords

def find_horizontal_path(grid):
	horCoords = [(0,0) for x in range(width(grid))]
	totals = [0 for x in range(height(grid))]
	totalCount = 0
	horGrid = energy(grid)
	totalEnergy = 0
	lowest = horGrid[0][0]
	k = 1
	totalReturn = 0
	up = 0
	r = 0 #setting row number
	
	#figuring out which value to start with	
	for h in range (height(grid)):
		r = h
		horCoords[0] = (h,0)
		for k in range (1,width(grid)): #moving across the grid
			nextCoord = horGrid[r][k]
			if r > 0 and horGrid[r-1][k] <= nextCoord:
				if r < (height(grid)-1) and horGrid[r+1][k] < horGrid[r-1][k]:
					r = r + 1
					up = 1
				else:
					r = r-1
			elif r < (height(grid)-1) and horGrid[r+1][k] < nextCoord and up < 1:
				r = r+1
			up = 0
			horCoords[k] = (r,k)
			k = k + 1
		#computing the values that each starting point will provide
		for l in range(width(grid)):
			totalEnergy = totalEnergy + int(energy_at(grid, int(horCoords[l][0]), int(horCoords[l][1])))
		totals[totalCount] = totalEnergy
		totalCount = totalCount + 1
		totalEnergy = 0
		horCoords = [(0,0) for x in range(width(grid))]
	minValue = totals[0]
	for p in range (height(grid)):
		if(totals[p] < minValue):
			totalReturn = p
			minValue = totals[p]
	horCoords[0] = (totalReturn, 0)
	r = totalReturn		

	#starting at the proper spot and coputing the delete array				 
	for k in range (1,width(grid)): #moving across the grid
		nextCoord = horGrid[r][k]
		if r > 0 and horGrid[r-1][k] <= nextCoord:
			if r < (height(grid)-1) and horGrid[r+1][k] < horGrid[r-1][k]:
				r = r + 1
				up = 1
			else:
				r = r-1
		elif r < (height(grid)-1) and horGrid[r+1][k] < nextCoord and up < 1:
			r = r+1
		up = 0
		horCoords[k] = (r,k)
		k = k + 1
		
	return horCoords

def remove_vertical_path(grid, path):
	for i in range (height(grid)):
		del grid[(path[i][0])][(path[i][1])]
	return grid


def remove_horizontal_path(grid, path):
	for i in range (width(grid)):
		grid[(path[i][0])][(path[i][1])] = (-1,i,-1)
	grid = list(map(list,zip(*grid))) #transposing grid
	for k in range (height(grid)):
		del grid[(path[k][1])][(path[k][0])]
	grid = list(map(list,zip(*grid))) #returning grid to normal state
	return grid

#reading lines and erasing comment lines
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
	return data2

#Given the name of a ppm file, open it up, read past the header information
#and then read all the RGB values into a grid of RGB triplets. Return that grid.
def ppm_to_grid(filename):
	data = read_lines(filename)
	rgbstring = ""
	col = data[1]
	row = data[2]
	maxValue = data[3]
	for k in range(4,len(data)):
		rgbstring += str(data[k])
	data2 = rgbstring.split()
	rgblength = int(row) * int(col)
	datacount = -1
	

	rgbcoords = [(0,0,0) for x in range(rgblength)]
	for k in range(rgblength):
		datacount += 1
		num1 = data2[datacount]
		datacount += 1
		num2 = data2[datacount]
		datacount += 1
		num3 = data2[datacount]
		rgbcoords[k] = (int(num1), int(num2), int(num3))
	
	#HAVE TO SEPERATE BY ROWS. PUTTING EACH ROW INTO A INDEX OF A 2D LIST
	finalMatrix = [[0 for x in range(int(col))] for x in range(int(row))]
	colCount = 0
	rowCount = 0
	
	for h in range(len(rgbcoords)):
		
		finalMatrix[rowCount][colCount] = rgbcoords[h]
		colCount += 1
		if(colCount==(int(col))):
			rowCount += 1
			colCount = 0
	return finalMatrix		
	
#Given a grid of RGB triplets, write out a ppm file to the given filename and save it.
def grid_to_ppm(grid, filename):
	f = open(filename, 'w')
	f.write('P3\n')
	f.write(str(width(grid)) + '\n')
	f.write(str(height(grid)) + '\n')
	f.write('255\n')
	totalCoords = height(grid) * width(grid) * 3
	for k in range(height(grid)):
		for h in range(width(grid)):
			f.write(str(grid[k][h][0])+'\n')		
			f.write(str(grid[k][h][1])+'\n')	
			f.write(str(grid[k][h][2])+'\n')
	f.close()		
	



