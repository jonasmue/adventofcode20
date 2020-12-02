import os

SKELETON_FILES = ["part1.py", "part2.py", "common.py", "input.txt", "README.md"]

current_day = int(sorted([file for file in os.listdir() if "day" in file])[-1][-2:])
next_day = current_day + 1
next_day_str = "day"
next_day_str += "0{}".format(next_day) if next_day < 10 else str(next_day)

os.mkdir(next_day_str)
os.chdir(next_day_str)
for f in SKELETON_FILES:
	with open(f, 'w'): pass
