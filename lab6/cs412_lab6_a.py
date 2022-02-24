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
    storage = [None] * (len(word) +1)
    def countPalis(word, index):
        right = word[index:]
        if storage[index]:
            return storage[index]
        count = 0
        if len(right) <= 1:
            return 1
        for i in range(1, len(right)+1):
            #print(i)
            if isPalindrome(right[:i]):
                count += countPalis(word, i + index)
        storage[index] = count
        return count
    return countPalis(word, 0)
    
def isPalindrome(pal):
    return pal == pal[::-1]

if __name__ == "__main__":
    main()