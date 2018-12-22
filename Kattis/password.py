
def main():
    n = int(input())
    lst = []
    s = 0
    for i in range(n):
        lst.append(float((input().split())[1]))

    lst.sort(reverse=True)

    for i in range(len(lst)):
        s += (i+1)*lst[i]

    print("{:.4f}".format(s))

main()
