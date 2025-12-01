import re
import sys; args = sys.argv[1:]

instructions = open(args[0]).readlines()
sum = 0
enabled = True
for inst in instructions:
    for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", inst):
        if i == "do()":
            enabled = True
        elif i == "don't()":
            enabled = False
        elif enabled:
            x, y = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", i).groups()
            sum += int(x) * int(y)
print(sum)
