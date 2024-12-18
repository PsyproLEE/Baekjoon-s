import sys

m = int(sys.stdin.readline())
S = set()

for i in range(m):
    commands = sys.stdin.readline().strip().split()
    if len(commands) == 1:
        if commands[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    else:
        command, num = commands[0], int(commands[1])
        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check" :
            print(int(num in S))
        elif command == "toggle" :
            if num in S:
                S.discard(num)
            else:
                S.add(num)


