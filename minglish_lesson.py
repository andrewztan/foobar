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

def answer(words):
    # print(words)
    graph = make_graph(words)
    # print(graph)
    start = start_vertex(graph)
    # print(start)

    letters = []
    seen = []

    # DFS postorder graph traversal
    def traverse(vertex):
        if vertex not in seen:
            seen.append(vertex)
            if vertex in graph:
                for edge in graph[vertex]:
                    traverse(edge)
            letters.append(vertex)

    traverse(start)

    # topological sort - reverse DFS postorder
    ordered = letters[::-1]
    alphabet = stringify(ordered)
    return alphabet

def stringify(letters):
    alphabet = ''
    for letter in letters:
        alphabet += letter
    # print(alphabet)
    return alphabet

def make_graph(words):
    graph = {}
    for i in range(1, len(words)):
        pair = find_edge(words[i-1], words[i])
        # print(pair)
        if pair is not None:
            vertex, edge = pair
            if vertex in graph:
                # add edge to vertex
                graph[vertex].append(edge)
            else:
                # create vertex, edge pair
                graph[vertex] = [edge]
    return graph

def find_edge(a, b):
    l = min(len(a), len(b))
    for i in range(l):
        if a[i] != b[i]:
            return a[i], b[i]

def start_vertex(graph):
    edges = []
    for values in graph.values():
        for val in values:
            edges.append(val)
    for vertex in graph:
        if vertex not in edges:
            return vertex

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