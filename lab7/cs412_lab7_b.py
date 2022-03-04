def main():
    weightLimit = int(input())
    itemNum = int(input())
    storage = [[None for i in range(3)] for j in range(itemNum)]
    #NOT ACTUALLY CHANGING THEM TO TUPLES
    for i in range(itemNum):
        toTuple = [x for x in input().split(" ")]
        # makes everything that isn't the strings into ints
        toTuple[1], toTuple[2] = float(toTuple[1]), float(toTuple[2])
        storage[i] = toTuple
        
        #print(toTuple)
    # SORT BY COST RATIO, APPARENTLY EASY TO DO LOL
    storage.sort(key=lambda col: (col[1]//col[2]), reverse = True)
    inThere = [False for _ in range(len(storage))]
    #print(storage)

    # FINDING THE ITEMS ACTUALLY IN THE BAG
    def findItems(weightLimit):
        value = 0
        # THIRD IS THE WEIGHT, ALREADY SORTED, DON'T WORRY ABOUT COST
        for i in range(len(storage)):
            # THE THING FITS
            #print(storage[i])
            if weightLimit - storage[i][2] >= 0:
                weightLimit -= storage[i][2]
                #print(weightLimit)
                value += storage[i][1]
                inThere[i] = True
            # IF IT ALL DOESN"T FIT, TAKE A FRACTION
            else:
                #THIS PRESUMABLY ZEROES OUT THE BAG IF IT DOESN'T ALL FIT
                someOfIt = weightLimit / storage[i][2]
                value += storage[i][1] * someOfIt
                weightLimit = int(weightLimit - (storage[i][2] * someOfIt))
                # IF IT'S ZERO, NO NEED TO DO THE OTHER THINGS
                inThere[i] = True
                break
        return value
        #print(value)

    value = findItems(weightLimit)

    #print(inThere)
    for i in range(len(storage)):
        if inThere[i]:
            print(storage[i][0], end="(")
            print(storage[i][1], end=", ")
            print(storage[i][2], end=") ")
    print()
    print(value)



if __name__ == "__main__":
    main()