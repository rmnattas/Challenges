import sys

def isInt(s):
    try:
        int(s)
        return True
    except:
        return False


def intToWord(s):
    units = { 0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 :
    "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine" }

    ten = { 0 : "ten", 1 : "eleven", 2 : "twelve", 3 : "therteen", 4 :
    "fourteen", 5 : "fifteen", 6 : "sixteen", 7 : "seventeen", 8 : "eighteen",
    9 : "nineteen" }

    tens = { 2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty",
    7 : "seventy", 8 : "eighty", 9 : "ninety" }

    s = int(s)
    if (s < 10):
        return units[s]
    elif (s < 20):
        return ten[s]
    else:
        if (s%10 == 0):
            return tens[s//10]
        else:
            return tens[s//10] + "-" + units[s%10]


def main():

    try:
        line = input().split()
    except:
        return

    while True:
        for i in range(len(line)):
            if (isInt(line[i])):
                line[i] = intToWord(line[i])
                if (i == 0): line[i] = (line[i][0].upper() + line[i][1:])
        print(" ".join(line))

        try:
            line = input().split()
        except:
            break
    

import sys

lo = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

hi = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def to_words(n):
    if n < 20:
        return lo[n]
    if n % 10 == 0:
        return hi[n // 10]
    return "-".join([hi[n // 10], lo[n % 10]])


for line in sys.stdin:
    s = " ".join([word if not word.isdigit() else to_words(int(word)) for word in line.split()])
    print(s[0].upper() + s[1:])
