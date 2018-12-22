

def main():
    i = 1
    while(True):
        line_in = input()
        if line_in == "END":
            break
        line = [x for x in line_in.split("*")]
        line.pop(0)
        line.pop()
        if len(line) <= 0:
            print(i, "EVEN")
            i += 1
            continue
        done = False
        for j in range(len(line)-1):
            if line[j] != line[j+1]:
                print(i, "NOT EVEN")
                done = True
                break
        if not done:
            print(i, "EVEN")
        i += 1

main()

