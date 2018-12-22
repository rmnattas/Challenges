

def main():
    m = int(input())
    winners = []

    for i in range(m):
        line = input()
        sline = [x for x in line.split()]
        if sline[0] not in winners:
            print(line)
            winners.append(sline[0])
        if len(winners) == 12:
            break



main()

