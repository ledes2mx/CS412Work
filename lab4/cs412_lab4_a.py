# Miguel Ledesma

def main():
    n = int(input())
    lines = []
    for _ in range (n):
        lines = lines + [input()]
    #print(lines)
    for i in range (len(lines)):
        print(paliCheck(lines[i]))

def paliCheck(word):
    count = 0
    count2 = 0
    for i in range(len(word)):
        left = word[:i+1]
        right = word[i+1:]
        """
        print("LEFT")
        print(left)
        print("RIGHT")
        print(right)
        """
        if isPalindrome(left):
            #print("COUNT")
            count += 1
        else:
            count2 = paliCheck(word[i:])
            if count2 > 1:
                count += count2 - 1
        #print(count)
    return count

        

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