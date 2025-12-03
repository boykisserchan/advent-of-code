import re
import sys;
from linecache import cache

from PIL.SpiderImagePlugin import iforms
from numpy.ma.core import maximum

args = sys.argv[1:]

list = open(args[0]).readlines()
# sum = 0
# for bat in list:
#     maxi = -1
#     battery = [int(i) for i in bat.strip()]
#     for i, b in enumerate(battery):
#         if not battery[i+1:]: continue
#         maxiRemBat = max(battery[i+1:])
#         maxi = max(maxi, b * 10 + maxiRemBat)
#     sum += maxi
sum = 0
for bat in list:
    battery = [int(i) for i in bat.strip()]
    largest12 = sorted(battery, reverse=True)[:12]
    print(largest12)
    largest12dct = {i: largest12.count(i) for i in largest12}
    largest12bat = ""

    print(len(largest12bat))

    sum += int(''.join(largest12bat))


print(sum)