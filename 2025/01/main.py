import sys; args = sys.argv[1:]

list = open(args[0]).readlines()
it = [(n[0], int(n[1:])) for n in list]
count = 0
dial = 50
for d, c in it:
    for _ in range(c):
        dial += -1 if d == "L" else 1
        dial = dial % 100
        if dial == 0:
            count += 1
print(count)