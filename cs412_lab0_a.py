"""
    name:  Your name(s) here
    
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    n = int(input())
    lines = [input().split(" ") for _ in range(n)]
    for line in lines:
        print(line[0], ":", line[1])

if __name__ == "__main__":
    main()