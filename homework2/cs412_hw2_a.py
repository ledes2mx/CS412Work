import re
import sys


def main():
    maxVal = ~sys.maxsize
    minVal = sys.maxsize
    equation = re.split('(\+|\*|\-)', input())
    
    print(equation)

if __name__ == "__main__":
    main()