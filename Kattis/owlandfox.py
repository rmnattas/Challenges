

def main():
    m = int(input())

    for _ in range(m):
        number = int(input())
        zeros = 0
        x = number
        while (x % 10) == 0:
            x /= 10
            zeros +=1
        print(number - 1*(10**zeros))


main()

