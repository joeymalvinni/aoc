groups = open(0).read().strip().split(",")

total = 0

for x in groups:
    curr = 0
    for ch in x:
        curr += ord(ch)
        curr *= 17
        curr %= 256

    total += curr

print(total)
