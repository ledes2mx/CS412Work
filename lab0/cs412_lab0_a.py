"""
    name:  Miguel Ledesma & Quade Curry
    
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