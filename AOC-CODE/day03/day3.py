import re
input_file = "input.txt"
try:
    with open(input_file, "r") as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    exit(1)
part1 = 0
part2 = 0
enabled = True
for inst in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data):
    match inst:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            x, y = map(int, inst[4:-1].split(","))
            part1 += x * y
            if enabled:
                part2 += x * y
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
