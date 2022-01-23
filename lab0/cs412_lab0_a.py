"""
    name:  Miguel Ledesma

    1. I used a dictionary as my only data structure.

    2. I used a store and a lookup

    3. Both are O(1) worst case since lookups and storage are both constant time operations.

    4. O(m + n) because m is the storage of the key and m is the lookup of a word. these two happen at different times.

    5. It works because the input is always going to be in the same format, that being a number, (for the number of lines to add to the dictionary)
    the lines actually added to the dictionary, then the words to look up in the dictionary at the end.

    
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
# call input to read next line

def main():
    words = {}
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        words[line[1]] = line[0]
    last = input().split(" ")
    for word in last:
        if word in words:
            print(words[word], end=' ')
        else:
            print("???", end=' ')
    print()

if __name__ == "__main__":
    main()