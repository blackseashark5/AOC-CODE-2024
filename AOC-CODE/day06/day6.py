import sys
def get_start():
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)
input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
try:
    with open(input_file, "r") as f:
        grid = list(map(list, map(str.strip, f.readlines())))
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
num_rows = len(grid)
num_cols = len(grid[0])

r, c = get_start()
dr, dc = -1, 0
visited = set()
while True:
    visited.add((r, c))
    if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
        break
    if grid[r + dr][c + dc] == "#":
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc
print(f"Part 1: {len(visited)}")
start_r, start_c = get_start()
def check_for_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()
    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if grid[ro][co] != ".":
            continue
        grid[ro][co] = "#"
        if check_for_loop():
            part2 += 1
        grid[ro][co] = "."

print(f"Part 2: {part2}")
