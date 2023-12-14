grid = open(0).read().splitlines()
coords = [(int(r), int(c)) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "O"]

for (r, c) in coords:
    while True:
        if r > 0:
            if grid[r-1][c] == ".":
                grid[r-1] = grid[r-1][:c] + "O" + grid[r-1][c+1:]
                grid[r] = grid[r][:c] + "." + grid[r][c+1:]
                r = r-1
            else:
                break
        else:
    break

total = 0
for r, row in enumerate(grid[::-1]):
    c = row.count("O")

    total += c * (r+1)
    
print(total)
