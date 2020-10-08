size = 7

free = -999

yPos = [free 
        for i in range(size)]

def check(x,y):
    for xi in range(size):
        if(yPos[xi] == y):
            return False
    for xi in range(size):
        if(xi+yPos[xi] == x+y):
            return False
    for xi in range(size):
        if(xi-yPos[xi] == x-y):
            return False
    return True
def main():
    for x in range(size):
        if(yPos[x] == free):
            for y in range(size):
                if check(x,y):
                    yPos[x] = y
                    main()
                    yPos[x] = free
            return
    gui(yPos)

def gui(y):
    n = ["-", "1", "2", "3", "4", "5", "6", "7", "8"]
    a = ["A", "█", "█", "█", "█", "█", "█", "█", "█"]
    b = ["B", "█", "█", "█", "█", "█", "█", "█", "█"]
    c = ["C", "█", "█", "█", "█", "█", "█", "█", "█"]
    d = ["D", "█", "█", "█", "█", "█", "█", "█", "█"]
    e = ["E", "█", "█", "█", "█", "█", "█", "█", "█"]
    f = ["F", "█", "█", "█", "█", "█", "█", "█", "█"]
    g = ["G", "█", "█", "█", "█", "█", "█", "█", "█"]
    h = ["H", "█", "█", "█", "█", "█", "█", "█", "█"]

    for idx,pos in enumerate(y):
        if idx == 0:
            a[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 1:
            b[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 2:
            c[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 3:
            d[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 4:
            e[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 5:
            f[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 6:
            g[pos] = "X"
    for idx,pos in enumerate(y):
        if idx == 7:
            h[pos] = "X"
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(" ".join(n))
    print(" ".join(a))
    print(" ".join(b))
    print(" ".join(c))
    print(" ".join(d))
    print(" ".join(e))
    print(" ".join(f))
    print(" ".join(g))
    print(" ".join(h))
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("\n")

main()