import sys
from collections import defaultdict
from functools import cmp_to_key
default_file = "input.txt"
input_file = sys.argv[1] if len(sys.argv) > 1 else default_file
try:
    with open(input_file, "r") as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
rules, jobs = data.split("\n\n")
rules = [tuple(map(int, l.split("|"))) for l in rules.splitlines()]
jobs = [tuple(map(int, l.split(","))) for l in jobs.splitlines()]

invalid_map = defaultdict(bool)
for x, y in rules:
    invalid_map[(y, x)] = True
def check_job(job: list[int]) -> bool:
    for i in range(len(job)):
        for j in range(i + 1, len(job)):
            if invalid_map[(job[i], job[j])]:
                return False
    return True
def sort_job(a: int, b: int) -> int:
    if invalid_map[(a, b)]:
        return 1
    return -1
part1 = 0
part2 = 0
for job in jobs:
    if check_job(job):
        part1 += job[len(job) // 2]
    else:
        fixed_job = sorted(job, key=cmp_to_key(sort_job))
        part2 += fixed_job[len(fixed_job) // 2]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
