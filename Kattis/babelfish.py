def main():
    line = input().split()
    d = {}
    while (line):
        d[line[1]] = line[0]
        line = input().split()


    line = input()
    while (line):
        if (line in d.keys()):
            print(d[line])
        else:
            print("eh")
        try:
            line = input()
        except:
            break


main()
