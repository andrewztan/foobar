"""
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight, and so on. Each string is one of: 

"L" : put weight on left-hand side 
"R" : put weight on right-hand side 
"-" : do not use weight 

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 2
Output:
    (string list) ["L", "R"]

Inputs:
    (int) x = 8
Output:
    (string list) ["L", "-", "R"]
"""
from math import log

def element(weight, index):
	prev = 0
	for i in range(index):
		prev += 3 ** i
	diff = weight - prev
	pos = diff % (3 ** (index + 1)) - 1 
	if  pos >= 0 and pos < 3 ** index:
		return "R"
	elif pos >= 3 ** index and pos < 2 * 3 ** index:
		return "L"
	else:
		return "-"
def answer(x):
	solution = []
	weight = 1
	n = int(log(x * 2, 3)) + 1
	for i in range(n):
		j = element(x, i)
		solution.append(j)
	return solution


# def test():
# 	t1 = 2
# 	t2 = 8
# 	assert ["L", "R"] == answer2(t1)
# 	assert ["L", "-", "R"] == answer2(t2)

# 	t3 = 10
# 	assert ["R", "-", "R"] == answer2(t3)

# test()
for i in range(1, 100):
	answer(i)

