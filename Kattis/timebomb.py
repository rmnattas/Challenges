
zero = [ "***", "* *", "* *", "* *", "***"]
one = [ "  *", "  *", "  *", "  *", "  *"]
two = [ "***", "  *", "***", "*  ", "***"]
three = [ "***", "  *", "***", "  *", "***"]
four = [ "* *", "* *", "***", "  *", "  *"]
five = [ "***", "*  ", "***", "  *", "***"]
six = [ "***", "*  ", "***", "* *", "***"]
seven = [ "***", "  *", "  *", "  *", "  *"]
eight = [ "***", "* *", "***", "* *", "***"]
nine = [ "***", "* *", "***", "  *", "***"]

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

def main():
    time_ascii = []
    time = 0
    for _ in range(5):
        time_ascii.append(input())
    
    m = (len(time_ascii[0])+1)//4
    
    for i in range(1, m+1):
        start_col = 4*(i-1)
        digit = []
        for j in range(5):
            digit.append(time_ascii[j][start_col:start_col+3])
        if digit in numbers:
            time += numbers.index(digit)
            time *= 10
        else:
            print("BOOM!!")
            return
    time //= 10

    if time % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")


main()

