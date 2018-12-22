from sys import stdin

def main():
    for line in stdin:
        line = line.split()
        sunrise = [int(x) for x in line[3].split(':')]
        sunset = [int(x) for x in line[4].split(':')]
        hours = sunset[0] - sunrise[0]
        minutes = sunset[1] - sunrise[1]
        if minutes >= 60:
            hours += 1
            minutes -= 60
        elif minutes < 0:
            hours -= 1
            minutes += 60
        print(" ".join(line[:3]), hours, "hours", minutes, "minutes")

main()

