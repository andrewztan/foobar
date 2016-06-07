"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.

Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1
"""
# def all_but_left(grid):
# 	new_grid = []
# 	for i in range(len(grid)):
# 		new_grid.append(grid[i][1:])
# 	return new_grid

# def answer(food, grid):
# 	row_len = len(grid[0])
# 	col_len = len(grid)
# 	if  row_len == 1 and col_len == 1:
# 		return food
# 	a, b = -1, -1
# 	# move down
# 	if col_len > 1:
# 		a = answer(food - grid[1][0], grid[1:])
# 	# move right
# 	if row_len > 1:
# 		b = answer(food - grid[0][1], all_but_left(grid))

# 	if a < 0 and b < 0:
# 		return -1
# 	elif a < 0:
# 		return b
# 	elif b < 0:
# 		return a
# 	else:
# 		return min(a, b)


import heapq

class Node:
	def __init__(self, food, position):
		self.food = food
		self.position = position
	def __lt__(self, other):
		return self.food < other.food

def answer(food, grid):
	col_len = len(grid)
	row_len = len(grid[0])
	pq = []
	heapq.heappush(pq, Node(food, (0,0)))
	while len(pq) > 0:
		top = heapq.heappop(pq)
		if top.position == (col_len - 1, row_len - 1):
			return top.food

		x = top.position[0]
		y = top.position[1]
		# move down
		if x + 1 < col_len:
			new_food = top.food - grid[x + 1][y]
			if new_food >= 0:
				heapq.heappush(pq, Node(new_food, (x + 1, y)))
		# move right 
		if y + 1 < row_len:
			new_food = top.food - grid[x][y + 1]
			if new_food >= 0:
				heapq.heappush(pq, Node(new_food, (x, y + 1)))

	return -1

def test():
	print(answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))
	assert 0 == answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
	print(answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))
	assert 1 == answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
test()
