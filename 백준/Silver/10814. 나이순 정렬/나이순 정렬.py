import sys
input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    N = int(data[0].strip())
    members = []

    for i in range(1, N + 1):
        age, name = data[i].split()
        members.append((int(age), i, name))
   
    members.sort(key=lambda x: (x[0], x[1]))


    for member in members:
        print(member[0], member[2])

if __name__ == "__main__":
    main()
