import re
import sys
from unittest import case


def main():
    maxVal = ~sys.maxsize
    minVal = sys.maxsize
    equation = re.split('(\+|\*|\-)', input())
    if len(equation) == 1:
        maxVal = int(equation[0])
        minVal = int(equation[0])
        print(minVal)
        print(maxVal)
    else:
        for i in range (1, len(equation), 2):
            op = equation[i]
            left = equation[:i]
            right = equation[i+1:]
            value = 0
            if op == '+':
                value = findVals(left) + findVals(right)
            if op == '*':
                value = findVals(left) * findVals(right)
            if op == '-':
                value = findVals(left) - findVals(right)
            if value < minVal:
                minVal = value
            if value > maxVal:
                maxVal = value
        for i in range(-2, -(len(equation)), -2):
            op = equation[i]
            left = equation[:i]
            right = equation[i+1:]
            value = 0
            if op == '+':
                value = findValsbw(left) + findValsbw(right)
            if op == '*':
                value = findValsbw(left) * findValsbw(right)
            if op == '-':
                value = findValsbw(left) - findValsbw(right)
            if value < minVal:
                minVal = value
            if value > maxVal:
                maxVal = value
        print(minVal)
        print(maxVal)

        
            

def findVals(equation):
    if len(equation) == 1:
        return int(equation[0])
    op = equation[1]
    left = equation[:1]
    right = equation[2:]
    value = 0
    if op == '+':
        value = findVals(left) + findVals(right)
    if op == '*':
        value = findVals(left) * findVals(right)
    if op == '-':
        value = findVals(left) - findVals(right)
    return value

def findValsbw(equation):
    if len(equation) == 1:
        return int(equation[0])
    op = equation[-2]
    left = equation[:-2]
    right = equation[-1:]
    value = 0
    if op == '+':
        value = findValsbw(left) + findValsbw(right)
    if op == '*':
        value = findValsbw(left) * findValsbw(right)
    if op == '-':
        value = findValsbw(left) - findValsbw(right)
    return value

    
        
        
    

if __name__ == "__main__":
    main()