def print_list(x):
    print(len(x))
    text = ''
    for g in x:
        text += str(g) + ' '
    print(text[:-1])

def main():
    m = int(input())
    line = [int(x) for x in input().split()]

    g = 0
    solution = []
    for i in range(m):
        if line[i] > g:
            solution.append(line[i])
            g = line[i]

    print_list(solution)


main()

