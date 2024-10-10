# Auto updating entropy by accessing neighbors entropy and determining ones own entropy based off of it?? probably not because entropy is decided based on available tile in the "possibilities" array
# MVC Structure, Adjacency List.
# 070000043040009610800634900094052000358460020000800530080070091902100005007040802
import sys
import random
# import runners package???


# Init grid of tiles
# Another option for storing the data is to make it a flat string of objects and just use basic math to figure out what indexs need manipulated.
class Grid:
	def __init__(self):
		self.data = [[Tile() for y in range(9)] for x in range(9)]
	# Init sudoku data here.


	def set(self, x, y, value):
		self.data[y][x] = value


class Tile:
	def __init__(self):
		self.val = None
		self.collapsed = False
		self.possibilities = {i for i in range(1, 10)}
		self.entropy = len(self.possibilities)

	def getPossibilities(self):
		return self.possibilities


#Take a Sudoku file as command line arg, read that file and interpolate it into a Grid object.

# Can make this cleaner by using an else statement after "if input.isnumeric()" instead of the code above it.
def preload(value):
	input = value
	if input.isnumeric() == False:
		ftype = input.split(".")
		ext = ftype[1]
		if ext == "csv":
			df = pd.read_csv(value)
			return df
		elif ext != "csv":
			raise Exception("File must be CSV")

	if input.isnumeric():
		if len(input) % 9 == 0:
			return input
	else:
		return Exception("Invalid Input: Input must be a filepath or a string of 81 integers")


# Grid init done in the class definition?
def main():
	def reset():
		del grid
		main()
	data = preload(sys.argv[1])
	grid = Grid()
	print("\nPartial Init Successful!")
	count = 0
	for y in range(9):
		for x in range(9):
			grid.data[y][x].val = int(data[count])
			count += 1
	print("\nFull Init successful!")

	#Step 1: If grid.data contains a tile with 0 entropy, reset and try again.
	#Step 2: Find the tile with the least entropy.
		#Step 2.5: If more than one tile with lowest entropy, then randomly select one
	#Step 3: If there is only one tile with the lowest entropy, then collapse tile
		#Step 3.5: If tile has only one [possibility] then collapse to that possibility, else randomly choose a possible tile
	#Step 4: Update entropy for tiles in the same row, column and 3x3 portion of the grid
	#Step 5: Repeat

	# Step 1 and 2. Should probably be a helper function.
	min = float('inf')
	lowest = []
	cur = None
	for y in range(9):
		for x in range(9):
			cur = grid.data[y][x]
			if cur.entropy == 0:
				return reset()
			if cur.collapsed == False:
				if cur.entropy < min:
					lowest.clear()
					min = cur.entropy
					lowest.append((y,x))
					print(lowest)
				elif cur.entropy == min:
					lowest.append((y,x))

	print("\nFind lowest entropy loop successful!")

	# Step 2.5: Choosing which tile in "lowest" to collapse
	yc, xc = random.choice(lowest)
	lowest.clear
	print("\nPick random lowest successful")

	# Step 3 and 3.5.
	if len(grid.data[yc][xc].possibilities) == 1:
		grid.data[yc][xc].val = grid.data[yc][xc].possibilities[0]
		grid.data[yc][xc].collapsed = True
	else:
		grid.data[yc][xc].val = random.choice(list(grid.data[yc][xc].possibilities))
		grid.data[yc][xc].collapsed = True

	print("\nAll segments successful!")


if __name__ == "__main__":
    main()

