import re
import sys


def main():
    maxVal = ~sys.maxsize
    minVal = sys.maxsize
    equation = re.split('(\+|\*|\-)', input())
    num = 0
    if len(equation) == 0:
        num = num + int(equation[0])
        minVal = num
        maxVal = num
    num = findVals(equation)

def findVals(equation):
    store = []
    if len(equation) == 1:
        num = int(equation[0])
        return num
    for i in range (1, len(equation), 2):
        op = equation[i]
        left = equation[:i]
        right = equation[i+1:]
        
        if op == '+':
            num = int(findVals(left) + findVals(right))
            #print(num)
        if op == '-':
            num = int(findVals(left) - findVals(right))
            #print(num)
        if op == '*':
            num = int(findVals(left) * findVals(right))
            #print(num)
        print("FINAL NUM")
        print(num)
    return num


if __name__ == "__main__":
    main()