def is_arithmetic(lst):
    dif = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i+1]-lst[i] != dif:
            return False
    return True

def sort(lst):
    lst.sort()
    return lst

def main():
    n = int(input())
    
    for _ in range(n):
        line = [int(x) for x in input().split()]
        m = line.pop(0)
        if is_arithmetic(line):
            print("arithmetic")
        elif is_arithmetic(sort(line)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")



main()

