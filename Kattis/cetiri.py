

def main():
    line = [int(x) for x in input().split()]
    line.sort()

    if (line[1] - line[0]) == (line[2] - line[1]):
        print(line[2] + (line[1]-line[0]))
    elif (line[1] - line[0]) < (line[2] - line[1]):
        print(line[1] + (line[1] - line[0]))
    else:
        print(line[0] + (line[2] - line[1]))
    

main()

