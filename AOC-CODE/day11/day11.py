import sys
from functools import cache
input_file = "input.txt"
if len(sys.argv) > 1:
    input_file = sys.argv[1]
try:
    with open(input_file, "r") as f:
        stones = list(map(int, f.read().strip().split(" ")))
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if val == 0:
        return count_stones(1, blinks - 1)
    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        return count_stones(int(str_val[: len_str_val // 2]), blinks - 1) + count_stones(int(str_val[len_str_val // 2 :]), blinks - 1)
    return count_stones(val * 2024, blinks - 1)
part1 = sum(count_stones(s, 25) for s in stones)
print(f"Part 1: {part1}")
part2 = sum(count_stones(s, 75) for s in stones)
print(f"Part 2: {part2}")
