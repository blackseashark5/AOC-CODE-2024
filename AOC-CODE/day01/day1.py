import sys
import os
default_file="input.txt"
input_file=sys.argv[1] if len(sys.argv)>1 else default_file
if not os.path.exists(input_file):
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)
with open(input_file,"r") as f:
    lines=[list(map(int,line.split())) for line in f.readlines()]
list1,list2=list(map(list,zip(*lines)))
part1=sum(abs(x1-x2) for x1,x2 in zip(sorted(list1),sorted(list2)))
print(f"Part 1: {part1}")
part2=sum(x*len([y for y in list2 if y==x]) for x in list1)
print(f"Part 2: {part2}")
