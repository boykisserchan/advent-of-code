import re
import sys; args = sys.argv[1:]

list = open(args[0]).read()
ranges = list.split(",")
ids = [map(int, i.split("-")) for i in ranges]
sum = 0
pattern = r"^(\d+?)\1+$"
for l, r in ids:
    for id in range(l, r):
        if re.match(pattern, str(id)):
            sum += id
print(sum)