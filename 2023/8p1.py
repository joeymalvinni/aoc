ma, _, *lines = open(0).read().splitlines()

m = {}
start = [x for x in lines if x.split(" = ")[0].endswith("A")][0].split(" = ")[0]
# print(start)

for val in lines:
    k, t = val.split(" = ")
    t = t[1:-1].split(", ")

    m[k] = t

steps = 1
curr = m[start][1 if ma[0] == "R" else 0]
ma = ma[1:] + ma[0] # push first instruction to end

while not curr.endswith("Z"):
    steps += 1
    curr = m[curr][1 if ma[0] == "R" else 0]

    ma = ma[1:] + ma[0]

print(steps)
