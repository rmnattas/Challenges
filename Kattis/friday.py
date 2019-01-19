


def main():
    cases = int(input())

    for _ in range(cases):
        days, months = [int(x) for x in input().split()]
        daysInMonths = [int(x) for x in input().split()]

        count = 0
        dayNumber = 1
        for month in daysInMonths:
            if (month > 12) and (((dayNumber+12) % 7) == 6):
                count += 1
            dayNumber += month
        print(count)


main()
