def report_safe(nums: list[int]) -> bool:
    diffs = [abs(x1 - x2) for x1, x2 in zip(nums, nums[1:])]
    if not all(1 <= d <= 3 for d in diffs):
        return False
    if all(x1 < x2 for x1, x2 in zip(nums, nums[1:])):
        return True
    if all(x1 > x2 for x1, x2 in zip(nums, nums[1:])):
        return True
    return False

def check_report(line: str, part1: bool = True) -> bool:
    nums = list(map(int, line.split(" ")))
    if report_safe(nums):
        return True
    if part1:
        return False
    for i in range(len(nums)):
        if report_safe(nums[:i] + nums[i + 1 :]):
            return True
    return False
input_file = "input.txt"

try:
    with open(input_file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

part1 = len([r for r in lines if check_report(r)])
print(f"Part 1: {part1}")

part2 = len([r for r in lines if check_report(r, part1=False)])
print(f"Part 2: {part2}")
