from sys import stdin

def main():
    for line in stdin:
        line = [int(x) for x in line.split()]
        for week_number in range(line[6]):
            eggs = line[0] * line[3]
            line[0] = line[1] // line[5]
            line[1] = line[2] // line[4]
            line[2] = eggs
        print(line[0])

main()

