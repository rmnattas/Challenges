from sys import stdin

def main():
    notes =  ["A#", "Bb", "C#", "Db", "D#", "Eb", "F#", "Gb", "G#", "Ab"]
    cnotes = ["Bb", "A#", "Db", "C#", "Eb", "D#", "Gb", "F#", "Ab", "G#"] 

    i = 1
    for line in stdin:
        print("Case " + str(i) + ": ", end="")
        line = line.split()
        if line[0] in notes:
            print(cnotes[notes.index(line[0])], line[1])
        else:
            print("UNIQUE")
        i += 1

main()

