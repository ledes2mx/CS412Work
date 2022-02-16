import sys

def main():
    parts = input().split(" ")
    length = int(input())
    minVal = sys.maxsize
    smallIndex = 0
    partsCollection = []
    #minParts = findParts(parts, length, -1)
    for i in range(-1,-(len(parts)+1), -1):
        partsCollection = partsCollection + [findParts(parts, length, i)]
    #print(partsCollection)
    for i in range(len(partsCollection)):
        if len(partsCollection[i]) < minVal:
            minVal = len(partsCollection[i])
            smallIndex = i
    smallest = partsCollection[smallIndex]
    #print(smallest)
    
    numParts = 0
    for part in parts:
        print(smallest.count(part), 'of length', part)
        numParts += smallest.count(part)
    print(numParts, 'rocket sections minimum')

def findParts(parts, length, index):
    if length == 0:
        return []
    if length - int(parts[index]) >= 0:
        #print(parts[index])
        #print("PART FITS")
        return [parts[index]] + findParts(parts, length-int(parts[index]), index)
    elif length - int(parts[index]) < 0:
        #print(parts[index])
        #print("PARt DOES NOT FIT")
        return findParts(parts, length, index-1)

if __name__ == "__main__":
    main()