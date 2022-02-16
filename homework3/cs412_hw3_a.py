def main():
    parts = input().split(" ")
    length = int(input())

    minParts = findParts(parts, length, -1)
    numParts = 0
    for part in parts:
        print(minParts.count(part), 'of length', part)
        numParts += minParts.count(part)
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