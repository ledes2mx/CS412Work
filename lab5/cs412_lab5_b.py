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
    def countPalis(word, index):
        count = 0
        if len(word) <= 1:
            return 1
        backend = word[index:]
        #print(backend)
        if len(backend) <= 1:
            #print("Last one")
            return 1
        for i in range(index+1, len(word)+1):
            #print(i)
            if isPalindrome(word[index:i]):
                count += countPalis(word, i)
        return count
    return countPalis(word, 0)
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