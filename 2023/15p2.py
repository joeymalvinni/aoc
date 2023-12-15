groups = open(0).read().strip().split(",")

def HASH(s):
    total = 0

    for ch in s:
        total += ord(ch)
        total *= 17
        total %= 256

    return total

boxes = {}
for seq in groups:
    if seq.endswith("-"):
        for i in boxes.keys():
            if boxes[i].get(seq[:-1]):
                del boxes[i][seq[:-1]]
    else:
        label, length = seq.split("=")
        h = HASH(label)
        if not boxes.get(h):
            boxes[h] = {}

            boxes[HASH(label)][label] = length

total = 0
for key in boxes.keys():
    for i, (label, length) in enumerate(boxes[key].items()):
        total += (key + 1) * (i + 1) * int(length)

print(total)
