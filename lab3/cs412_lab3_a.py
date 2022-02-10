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
    for i in range(len(word)):
        left = word[:i+1]
        right = word[i+1:]
        print(left)
        if isPalindrome(left):
            count += 1
        paliCheck(right, count)
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