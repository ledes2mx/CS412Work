from itertools import product

def confirmation(a, b, c):
    return ((a or b or c) and (a or b or not c) and (a or not b or c)
    and (a or not b or not c) and (not a or b or c)
    and (not a or b or not c) and (not a or not b or c)
    and (not a or not b or not c))

def missingConf(a, b, c):
    return ((a or b or c) and (a or b or not c) and (a or not b or c)
    and (a or not b or not c) and (not a or b or c)
    and (not a or b or not c) and (not a or not b or c))

def main():
    holder = product([True, False], repeat=3)
    missingHolder = product([True, False], repeat=3)
    for hold in holder:
        if confirmation(hold[0],hold[1],hold[2]):
            print(hold[0],hold[1],hold[2]) 
        else:
            print(False)
    for hold in missingHolder:
        if missingConf(hold[0],hold[1],hold[2]):
            print(hold[0],hold[1],hold[2]) 
        else:
            print(False)


if __name__ == "__main__":
    main()