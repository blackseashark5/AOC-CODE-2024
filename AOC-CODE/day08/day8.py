import sys
from collections import defaultdict
from itertools import combinations

# Use "input.txt" as default if no file is provided
input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

try:
    with open(input_file, "r") as f:
        lines = list(map(str.strip, f.readlines()))
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

antenna = defaultdict(set)
num_rows = len(lines)
num_cols = len(lines[0])

# Parse the input to identify antennas
for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != ".":
            antenna[val].add((r, c))

# Calculate antinodes
antinodes1 = set()
antinodes2 = set()
for freq in antenna:
    for (r1, c1), (r2, c2) in combinations(antenna[freq], 2):
        # Calculate symmetric points for antinodes1
        antinodes1.add((2 * r1 - r2, 2 * c1 - c2))
        antinodes1.add((2 * r2 - r1, 2 * c2 - c1))

        # Calculate lines for antinodes2
        dr = r2 - r1
        dc = c2 - c1
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r += dr
            c += dc
        r, c = r1, c1
        while 0 <= r < num_rows and 0 <= c < num_cols:
            antinodes2.add((r, c))
            r -= dr
            c -= dc

# Part 1: Count valid antinodes1 points within bounds
part1 = len([1 for r, c in antinodes1 if 0 <= r < num_rows and 0 <= c < num_cols])
print(f"Part 1: {part1}")

# Part 2: Count all antinodes2 points
part2 = len(antinodes2)
print(f"Part 2: {part2}")
