if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    a,b,c = 0,0,0

    print([[a,b,c] for a in [i for i in range(x+1)] for b in [j for j in range(y+1)] for c in [k for k in range(z+1)] if a+b+c != n])