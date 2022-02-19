# Miguel Ledesma

def main():
    n = int(input())
    lines = []
    keeper = {}
    for _ in range (n):
        lines = lines + [input()]
    #print(lines)
    for i in range (len(lines)):
        print(paliCheck(lines[i], keeper))

def paliCheck(word, keeper):
    count = 0
    if len(word) <= 1:
        return 1
    if word in keeper:
        return keeper[word]
    for i in range(1, len(word) + 1):
        left = word[:i]
        if isPalindrome(left):
            count += paliCheck(word[i:], keeper)
    keeper[word] = count
    return count

def isPalindrome(pal):
    return pal == pal[::-1]

if __name__ == "__main__":
    main()