grid = open(0).read().splitlines()

empty_rows = [r for (r, row) in enumerate(grid) if "#" not in row]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

galaxies = [(r, c) for (r, row) in enumerate(grid) for (c, ch) in enumerate(row) if ch == "#"]

scale = 999999
total = 0

for i, (y1, x1) in enumerate(galaxies):
        for (y2, x2) in galaxies[:i]:
                # loop over each row and column between the two galaxies
                # add scale if the row/col is empty

                total += sum([scale if r in empty_rows else 1 for r in range(min(y1, y2), max(y1, y2))])
                total += sum([scale if c in empty_cols else 1 for c in range(min(x1, x2), max(x1, x2))])

print(total)
