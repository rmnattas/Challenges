
def main():

    persons = int(input())

    while persons:
        orders = {}

        for _ in range(persons):
            person = input().split()
            name = person[0]
            for item in person[1:]:
                if item in orders:
                    orders[item].append(name)
                else:
                    orders[item] = [name]

        for item in sorted(orders):
            print(item, " ".join(orders[item]))

        print()    
        persons = int(input())


main()
