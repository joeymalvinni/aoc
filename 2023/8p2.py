from math import lcm
ma, _, *lines = open(0).read().splitlines()

starting = [x.split(" = ")[0] for x in lines if x.split(" = ")[0].endswith("A")]
m = {}

# print(starting)

for val in lines:
    k, t = val.split(" = ")
    t = t[1:-1].split(", ")

    m[k] = t

paths = []

for node in starting:
    curr = node 
    distance = 0
    while not curr.endswith("Z"):
        distance += 1
        
        # print(ma)
        curr = m[curr][1 if ma[0]  == "R" else 0]
        ma = ma[1:] + ma[0]

    paths.append(distance)
 
print(lcm(*paths))
