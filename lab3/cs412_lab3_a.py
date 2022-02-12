# Miguel Ledesma

def main():
    n = int(input())
    lines = []
    for _ in range (n):
        lines = lines + [input()]
    print(lines)
    for i in range (len(lines)):
        print(paliCheck(lines[i], 0))

def paliCheck(word, count):
    count = 0
    count2 = 0
    for i in range(len(word)):
        left = word[:i+1]
        right = word[i+1:]
        
        print("LEFT")
        print(left)
        print("RIGHT")
        print(right)
        
        if isPalindrome(left):
            print("COUNT")
            count += 1
        count2 = paliCheck(right, 0)
    if 1 < count:
        return count -1
    else:
        return 1
        

    """
    for i in range(len(word)):
        section = word[start:i+1]
        print(section)
        if isPalindrome(section):
            print("It's a Palindrome!")
        else:
            start += 1
            paliCheck(word, start)
            sections = sections + [section]
    #print(sections)
    """

def isPalindrome(pal):
    return pal == pal[::-1]

if __name__ == "__main__":
    main()