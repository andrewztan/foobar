def answer(words):
    # print(words)
    g = make_g(words)
    # print(g)
    start = start_v(g)
    # print(start)

    letters = []
    seen = []

    # DFS postorder g traversal
    def traverse(v):
        if v not in seen:
            seen.append(v)
            if v in g:
                for e in g[v]:
                    traverse(e)
            letters.append(v)

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

def make_g(words):
    g = {}
    for i in range(1, len(words)):
        pair = make_e(words[i-1], words[i])
        # print(pair)
        if pair is not None:
            v, e = pair
            if v in g:
                # add e to v
                g[v].append(e)
            else:
                # create v, e pair
                g[v] = [e]
    return g

def make_e(a, b):
    l = min(len(a), len(b))
    for i in range(l):
        if a[i] != b[i]:
            return a[i], b[i]

def start_v(g):
    edges = []
    for values in g.values():
        for val in values:
            edges.append(val)
    for v in g:
        if v not in edges:
            return v

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