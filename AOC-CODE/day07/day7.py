import sys
def check_possible(target: int, nums: list[int], part2=False) -> bool:
    if len(nums) == 1:
        return target == nums[0]
    num = nums.pop()
    if target / num == target // num:
        if check_possible(target // num, nums[:], part2=part2):
            return True
    if target - num >= 0:
        if check_possible(target - num, nums[:], part2=part2):
            return True
    if not part2:
        return False
    target_str = str(target)
    num_str = str(num)
    if target_str.endswith(num_str) and len(target_str) > len(num_str):
        new_target = int(target_str[: -len(num_str)])
        if check_possible(new_target, nums[:], part2=part2):
            return True
    return False
input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
try:
    with open(input_file, "r") as f:
        lines = list(map(str.strip, f.readlines()))
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
part1 = 0
part2 = 0
for line in lines:
    target = int(line.split(":")[0])
    nums = list(map(int, line.split(": ")[1].split(" ")))
    if check_possible(target, nums[:]):
        part1 += target
    if check_possible(target, nums[:], part2=True):
        part2 += target
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
