"""
Line up the captives
====================

As you ponder sneaky strategies for assisting with the great rabbit escape, you realize that you have an opportunity to fool Professor Booleans guards into thinking there are fewer rabbits total than there actually are.

By cleverly lining up the rabbits of different heights, you can obscure the sudden departure of some of the captives.

Beta Rabbits statisticians have asked you for some numerical analysis of how this could be done so that they can explore the best options.

Luckily, every rabbit has a slightly different height, and the guards are lazy and few in number. Only one guard is stationed at each end of the rabbit line-up as they survey their captive population. With a bit of misinformation added to the facility roster, you can make the guards think there are different numbers of rabbits in holding.

To help plan this caper you need to calculate how many ways the rabbits can be lined up such that a viewer on one end sees x rabbits, and a viewer on the other end sees y rabbits, because some taller rabbits block the view of the shorter ones.

For example, if the rabbits were arranged in line with heights 30 cm, 10 cm, 50 cm, 40 cm, and then 20 cm, a guard looking from the left side would see 2 rabbits (30 and 50 cm) while a guard looking from the right side would see 3 rabbits (20, 40 and 50 cm). 

Write a method answer(x,y,n) which returns the number of possible ways to arrange n rabbits of unique heights along an east to west line, so that only x are visible from the west, and only y are visible from the east. The return value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1 and as large as the total number of rabbits (n).

Test cases
==========

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Output:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Output:
    (string) "24"
"""

import math.factorial

def answer(x, y, n):
    return str(solve(x, y, n))

def solve(x, y, n):
    if x + y > n + 1 or (x == 1 and y == 1):
        return 0
    if x + y == n + 1:
        if x == n or y == n:
            return 1
        else:
            return n - x + n - y
    a = min(x, y)
    b = max(x, y)

def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n-r)


def test():
    x = 1
    y = 1
    n = 1
    assert "1" == answer(x, y, n)
    x = 1
    y = 1
    n = 3
    assert "0" == answer(x, y, n)
    x = 1
    y = 2
    n = 3
    assert "1" == answer(x, y, n)
    x = 1
    y = 3
    n = 3
    assert "1" == answer(x, y, n)
    x = 2
    y = 2
    n = 3
    assert "2" == answer(x, y, n)
    x = 2
    y = 3
    n = 3
    assert "0" == answer(x, y, n)
    x = 3
    y = 3
    n = 3
    assert "0" == answer(x, y, n)
    x = 1
    y = 2
    n = 6
    assert "24" == answer(x, y, n)
    x = 2
    y = 3
    n = 5
    assert "8" == answer(x, y, n)
    x = 3
    y = 3
    n = 5
    assert "4" == answer(x, y, n)
    x = 2
    y = 3
    n = 4
    assert "3" == answer(x, y, n)

def solve_one_side(x, n):
    if x > n:
        return 0
    elif x == 1:
        return factorial(n - 1)
    elif x == n:
        return 1

    start = x
    end = n
    r = n - x
    total = 0
    for i in range(start, end + 1):
        total += solve_one_side(x - 1, i - 1) * nCr(n - 1, i - 1) * factorial(n - i)
    return total

# test()
def test_one_side():
    x = 1
    n = 1
    # print (solve_one_side(x, n))
    assert 1 == solve_one_side(x, n)
    x = 2
    n = 3
    assert 3 == solve_one_side(x, n)
    x = 1
    n = 5
    assert 24 == solve_one_side(x, n)
    x = 5
    n = 5
    assert 1 == solve_one_side(x, n)
    x = 2
    n = 4
    assert 11 == solve_one_side(x, n)
    # _ 4 _ _ = 6 = 3 * 1 * 2
    # _ _ 4 _ = 3 = 3 * 1 * 1
    # _ _ _ 4 = 2 = 1 * 2 * 1
    """
    1. set max 
    2. do nCr on # in total choose # on left - (C)
    3. # of valid combinations on left solve_one_side(x - 1, # on left) - (S)
    4. # of permuations on left (factorial # on right) - (P)
    C * S * P
    """

test_one_side();

