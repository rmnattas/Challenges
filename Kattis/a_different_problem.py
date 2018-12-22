numbers = [int(x) for x in input().split()]
while numbers:
    print(abs(numbers[1]-numbers[0]))
    try:
        numbers = [int(x) for x in input().split()]
    except:
        break
