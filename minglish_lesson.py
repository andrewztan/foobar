"""
Minglish lesson
===============

Welcome to the lab, minion. Henceforth you shall do the bidding of Professor Boolean. Some say he's mad, trying to develop a zombie serum and all... but we think he's brilliant! 

First things first - Minions don't speak English, we speak Minglish. Use the Minglish dictionary to learn! The first thing you'll learn is how to use the dictionary.

Open the dictionary. Read the page numbers, figure out which pages come before others. You recognize the same letters used in English, but the order of letters is completely different in Minglish than English (a < b < c < ...).

Given a sorted list of dictionary words (you know they are sorted because you can read the page numbers), can you find the alphabetical order of the Minglish alphabet? For example, if the words were ["z", "yx", "yz"] the alphabetical order would be "xzy," which means x < z < y. The first two words tell you that z < y, and the last two words tell you that x < z.

Write a function answer(words) which, given a list of words sorted alphabetically in the Minglish alphabet, outputs a string that contains each letter present in the list of words exactly once; the order of the letters in the output must follow the order of letters in the Minglish alphabet. 

The list will contain at least 1 and no more than 50 words, and each word will consist of at least 1 and no more than 50 lowercase letters [a-z]. It is guaranteed that a total ordering can be developed from the input provided (i.e. given any two distinct letters, you can tell which is greater), and so the answer will exist and be unique.


Test cases
==========

Inputs:
    (string list) words = ["y", "z", "xy"]
Output:
    (string) "yzx"

Inputs:
    (string list) words = ["ba", "ab", "cb"]
Output:
    (string) "bac"
"""
def get_first_letters(words):
	if len(words) == 0:
		return []
	first_letters = []
	first_letters.append(words[0][0])
	for i in range(1, len(words)):
		if words[i][0] != words[i - 1][0]:
		first_letters.append(words[i][0]) 
	return first_letters;

def alphabet(words, dictionary):
	first_letters = get_first_letters(words)

def answer(words):
	return alphabet(words, [])

def test():
	words = ["z", "yx", "yz"]
	assert answer(words) == "xzy"
	words = ["y", "z", "xy"]
	assert answer(words) == "yzx"
	words = ["ba", "ab", "cb"]
	assert answer(words) == "bac"

test()

