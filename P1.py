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
