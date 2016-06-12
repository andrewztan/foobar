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

def get_first_letters(w):
    words = []
    for i in range(len(w)):
        if len(w[i]) > 0:
            words.append(w[i])
    if len(words) == 0:
        return []
    first_letters = []
    first_letters.append(words[0][0])
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][0]:
            first_letters.append(words[i][0]) 
    return first_letters;

# similar to the merge part of merge sort
def combine(lst1, lst2):
    combined = []
    i = 0
    j = 0
    k = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] in lst2:
            if lst2.index(lst1[i]) > j:
                combined.append(lst2[j])
                j += 1    
            elif lst2.index(lst1[i]) == j:
                combined.append(lst1[i])
                i += 1
                j += 1
            else:
                i += 1
            k += 1
        elif lst2[j] in lst1:
            if lst1.index(lst2[j]) > i:
                combined.append(lst1[i])
                i += 1
            elif lst1.index(lst2[j]) == j:
                combined.append(lst1[i])
                i += 1
                j += 1
            else:
                combined.append(lst2[j])
                j += 1
            k += 1
        else:
            i += 1
            j += 1
    if i < len(lst1):
        combined += lst1[i:]
    if j < len(lst2):
        combined += lst2[j:]
    return combined

def alphabet(words, dictionary):
    first_letters = get_first_letters(words)
    alphabet_list = combine(first_letters, dictionary)
    if len(first_letters) == len(words):
        return alphabet_list
    next_words = [words[0][1:]]
    for i in range(1, len(words)):
        if len(words[i]) > 1:
            if words[i][0] == words[i-1][0]:
                next_words.append(words[i][1:])
            else:
                if len(next_words) > 1:
                    alphabet_list = alphabet(next_words, alphabet_list)
                next_words = [words[i][1:]]
    if len(next_words) > 1:
        alphabet_list = alphabet(next_words, alphabet_list)
    return alphabet_list

def answer(words):
    alphabet_list = alphabet(words, [])
    alphabet_string = ""
    for letter in alphabet_list:
        alphabet_string += letter
    return alphabet_string


def test():
    words = ["z", "yx", "yz"]
    assert answer(words) == "xzy"
    words = ["y", "z", "xy"]
    assert answer(words) == "yzx"
    words = ["ba", "ab", "cb"]
    assert answer(words) == "bac"
    words = ["abc", "acd", "bcc", "bcd"]
    assert answer(words) == "abcd"

test()

