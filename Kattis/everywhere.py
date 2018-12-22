

def main():
    cases = int(input())
    for _ in range(cases):
        cities = []
        counter = 0
        n = int(input())
        for i in range(n):
            city = input()
            if city not in cities:
                counter += 1
                cities.append(city)
        print(counter)

main()
