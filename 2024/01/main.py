import sys; args = sys.argv[1:]

list = open(args[0]).read().split()
leftList = sorted([int(i) for i in list[::2]])
rightList = sorted([int(i) for i in list[1::2]])

sum = sum(leftList[i] * rightList.count(leftList[i]) for i in range(len(leftList)))

print(sum)