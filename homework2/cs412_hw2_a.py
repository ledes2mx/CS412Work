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
    for i in num:
        if minVal > i:
            minVal = i
        if maxVal < i:
            maxVal = i
    print(minVal, end=" ")
    print(maxVal)

def findVals(equation):
    finalStore = []
    store1 = []
    store2 = []
    if len(equation) == 1:
        temp = [int(equation[0])]
        return temp
    for i in range (1, len(equation), 2):
        op = equation[i]
        left = equation[:i]
        right = equation[i+1:]
        store1 = findVals(left)
        store2 = findVals(right)
        for j in store1:
            for k in store2:
                if op == '+':
                   finalStore = finalStore +  [j + k]
                    #print(num)
                if op == '-':
                    finalStore = finalStore +  [j - k]
                    #print(num)
                if op == '*':
                    finalStore = finalStore +  [j * k]
                    #print(num)
    return finalStore


if __name__ == "__main__":
    main()