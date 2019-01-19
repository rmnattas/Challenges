
def main():
    cases = int(input())
    
    for case in range(cases):
        print("Recipe # " + str(case+1))
        items, portions, desired = [int(x) for x in input().split()]


        ingredients = []
        for _ in range(items):
            ingredients.append([x for x in input().split()])


        # calculate scaled weight
        scaled_weight = 0
        for ingredient in ingredients:
            if float(ingredient[2]) == 100:
                scaled_weight = float(ingredient[1]) * (desired/portions)
                break

        
        for ingredient in ingredients:
            print("{} {:.1f}".format(ingredient[0], ( float(ingredient[2])*scaled_weight/100 )))
        
        print("-"*40)


main()
