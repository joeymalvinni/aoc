from collections import Counter

m = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

lines = [i for i in open('in.txt').read().split('\n') if i.strip()]

arr = []

for l in lines:
    hand, bid = l.split()
    bid = int(bid)
    arr.append((hand, bid))

def strength(x):
    c = Counter(x[0])
    # print(list(c.values()))

    a = sorted(list(c.values()))
    b = [m.get(p, p) for p in x[0]]
    # print(a, b)
    if (a == [1, 1, 1, 1, 1]):
        return (1, b)
    elif (a == [1, 1, 1, 2]):
        return (2, b)
    elif (a == [1, 2, 2]):
        return (3, b)
    elif (a == [1, 1, 3]):
        return (4, b)
    elif (a == [2, 3]):
        return (5, b)
    elif (a == [1, 4]):
        return (6, b)
    elif (a == [5]):
        return (7, b)


arr.sort(key=lambda x: strength(x))

total = 0

for i, el in enumerate(arr):
    total += (i+1) * el[1]

print(total)
