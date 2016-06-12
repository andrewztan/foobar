import random

"""
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you must compute how much standing water has accumulated on the rabbit hutches. 

Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as a list, computes the total area of standing water accumulated when water is poured from the top and allowed to run off the sides. 

The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1, and at most 100000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5

Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
"""

def answer(heights):
	"""
	Uses 3 arrays
	1. left: Array holding the max value of everything to the left of the index including the index
	2. right: Array holding the max value of everything to the right of the index
	3. water: Array holding the amount of water at that index
	Solution is the sum of Array 3

	Example:
	heights =     [6, 8, 6, 6, 9, 7, 10, 0, 2, 4] -> 12
	left =  [6, 8, 8, 8, 9, 9, 10, 10, 10, 10]
	right = [8, 6, 6, 9, 7, 10, 0,  2,  4, null]
	water = [0, 0, 2, 2, 0, 2, 0,  4,  2,  0]

	clean = [8,  6,  6,  9,  7,  10, 0,  2,  4] -> 12
	left =  [8,  8,  8,  9,  9,  10, 10, 10, 10]
	right = [10, 10, 10, 10, 10, 4,  4,  4,  0]
	water = [0,  2,  2,  0,  2,  0,  4,  2,  0]

	"""

	if len(heights) <= 2:
		return 0

	start_index = find_start_index(heights)
	end_index = find_end_index(heights)
	if start_index == -1 or end_index == -1 or start_index >= end_index:
		return 0

	copy = heights[:]
	clean = copy[start_index:end_index + 1]
	# max_index = find_max_index(heights, start_index, end_index + 1)

	left = [clean[0]]
	right = [0]
	for i in range(1, len(clean)):
		left.append(max(left[i - 1], clean[i]))
		right = [max(right[0], clean[-i])] + right
	print(left)
	print(right)

	water = []
	for i in range(len(left)):
		if clean[i] < left[i] and clean[i] < right[i]:
			water.append(min(left[i], right[i]) - clean[i])
		else:
			water.append(0)
	print(water)
	return sum(water) 


"""Find the max index in a list from indexes start (inclusive) to end (exclusive)"""
def find_max_index(lst, start, end):	
	index = start
	largest = lst[start]
	for i in range(1, end):
		if lst[i] > largest:
			index = i
			largest = lst[i]
	return index

def find_start_index(lst):
	for i in range(len(lst) - 1):
		if lst[i] > lst[i + 1]:
			return i
	return -1

def find_end_index(lst):
	for i in range(len(lst) - 1, 0, -1):
		if lst[i] > lst[i - 1]:
			return i
	return -1


"""Generate a random list (building) with length l and max value h"""
def generate_list(l, h):
	lst = []
	for i in range(l):
		lst.append(random.randrange(0, h + 1))
	return lst


l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 2, 1]
l3 = [3, 2, 1, 2, 3]
l4 = generate_list(10, 10)

tests = []
tests.append([l1, l2, l3])
print("l1 should be 0")
print("My l1 is: " + str(solve(l1)))
print("")
print("l2 should be 0")
print("My l2 is: " + str(solve(l2)))
print("")
print("l3 should be 4")
print("My l3 is: " + str(solve(l3)))
print("")
print("l4:")
print(l4)
print("l4 should be idk")
print("My l4 is: " + str(solve(l4)))


l5 = [6, 8, 6, 6, 9, 7, 10, 0, 2, 4]
print(solve(l5))



