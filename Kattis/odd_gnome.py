

def main():
    m = int(input())

    for _ in range(m):
        line = [int(x) for x in input().split()]
        king = 0
        for i in range(1, line[0]):
            if line[i] != line[i+1]-1:
                king = i+1
                break
        
        print(i+1)


main()

