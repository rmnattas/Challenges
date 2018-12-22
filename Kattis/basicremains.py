def int2base(x, b):
    if x < b:
        return str(x)
    else:
        return str(int2base(x//b, b)) + str(x%b) 

def main():
    while True:
        line = [x for x in input().split()]

        if line == ['0']:
            break

        line[0] = int(line[0])
        
        a = int(line[1], line[0])
        b = int(line[2], line[0])
        print(int2base(a%b, line[0]))



main()

