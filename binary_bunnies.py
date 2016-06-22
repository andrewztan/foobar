"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid laboratory, you had to develop a system to track them, since some habitually continue to gnaw on the heads of their brethren and need extra supervision. For obvious reasons, you based your rabbit survivor tracking system on a binary search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and each, luckily enough, had a distinct age. For a given group, the first rabbit became the root, and then the next one (taken in order of rescue) was added, older ages to the left and younger to the right. The order that the rabbits returned to you determined the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation, and you need to make sure that all of the modifications or pathogens introduced by Professor Boolean are contained properly. Since the tree did not preserve the order of rescue, it falls to you to figure out how many different sequences of rabbits could have produced an identical tree to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers and returns a string representing the number (in base-10) of sequences that would result in the same tree as the given sequence.

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"



Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

            5
          /   \
         2     9
        /     /
       1     8 
"""

import math

class BST:

    def __init__(self, *items):
        self.root = None
        self.left = None
        self.right = None
        for i in items:
            self.add(i)

    def add(self, item):
        if not self.root:
            self.root = item
        elif item < self.root:
            if self.left:
                self.left.add(item)
            else:
                self.left = BST(item)
        else:
            if self.right:
                self.right.add(item)
            else:
                self.right = BST(item)


def permutate(t):
    if not t:
        return 1
    left_count = count(t.left)
    right_count = count(t.right)

    left_permutation = permutate(t.left)
    right_permutation = permutate(t.right)
    # print(left_permutation)
    # print(right_permutation)
    # print(left_count)
    # print(right_count)
    # print(nCr(left_count + right_count, left_count))
    return nCr(left_count + right_count, left_count) * left_permutation * right_permutation

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def count(t):
    if not t:
        return 0
    # print(123)
    return 1 + count(t.left) + count(t.right)

def answer(seq):
    """
    Solution finds the number of different DAGs (directed acyclic graphs) can be created.
    Directions of graph depends on the binary tree. There exists an arrow from each parent to child pair.
    """
    # print(permutate(BST(seq)))
    return str(permutate(BST(*seq)))



def test():
    seq = [5, 9, 8, 2, 1]
    assert '6' == answer(seq)
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert '1' == answer(seq)
    seq = [5, 9, 8, 2, 1, 10]
    assert '20' == answer(seq)


test()