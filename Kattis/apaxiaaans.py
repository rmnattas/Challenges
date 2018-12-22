

def main():
    line = list(input())

    i = 0
    while i < len(line)-1:
        if line[i] == line[i+1]:
            line.pop(i+1)
        else:
            i+=1

    for c in line:
        print(c, end='')
    print()

main()

