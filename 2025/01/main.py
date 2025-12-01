import sys; args = sys.argv[1:]

list = open(args[0]).read().split()
it = [(n[0], int(n[1:])) for n in list]
count = 0
dial = 50
for d, c in it:
    polarity = 1
    if d == "L":
        polarity *= -1
    for _ in range(c):
        dial += polarity
        dial = dial % 100
        if dial == 0:
            count += 1
print(count)
