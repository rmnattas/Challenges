

def main():
    m = int(input())
    line = [int(x) for x in input().split()]

    c=0
    s=0

    for n in line:
        if n >= 0:
            c += 1
            s += n

    print(s/c)


main()

