if __name__ == '__main__':
    N = int(input())

r = []
for i in range(N):
    line = input().split(" ")
    c = line[0]
    if(c == "insert"):
        r.insert(int(line[1]),int(line[2]))
    if(c == "print"):
        print(r)
    if(c == "remove"):
        r.remove(int(line[1]))
    if(c == "append"):
        r.append(int(line[1]))
    if(c == "sort"):
        r.sort()
    if(c == "pop"):
        r.pop()
    if(c == "reverse"):
        r=list(reversed(r))

