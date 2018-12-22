

def main():
    dogs = [int(x) for x in input().split()]
    heros = [int(x) for x in input().split()]
    dogA_cycle = dogs[0] + dogs[1]
    dogB_cycle = dogs[2] + dogs[3]

    for time in heros:
        dogA = False
        dogB = False

        if (time % dogA_cycle) <= dogs[0] and (time % dogA_cycle) > 0:
            dogA = True
        if (time % dogB_cycle) <= dogs[2] and (time % dogB_cycle) > 0:
            dogB = True
            
        if dogA and dogB:
            print("both")
        elif dogA or dogB:
            print("one")
        else:
            print("none")


main()

