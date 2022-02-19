# Miguel Ledesma

def main():
    n = int(input())
    lines = []
    for _ in range (n):
        lines = lines + [input()]
    #print(lines)
    for i in range (len(lines)):
        print(paliCheck(lines[i], 1))

def paliCheck(word, index):
    count = 0
    if len(word) <= 1:
        return 1
    for index2 in range(index, len(word)+1):
        left = word[:index2]
        if isPalindrome(left):
            count += paliCheck(word, index + 1)
    return count
    """
    count = 0
    if len(word) <= 1:
        return 1
    for i in range(1, len(word) + 1):
        left = word[:i]

        if isPalindrome(left):
            count += paliCheck(word[i:])

    return count
    """

def isPalindrome(pal):
    return pal == pal[::-1]

if __name__ == "__main__":
    main()