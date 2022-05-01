"""
lab 6 Miguel Ledesma
Algo analysis: This algorithm runs in O(n^2) time from
lines 14 to 17 
"""
def isPalindrone(s):
    return s == s[::-1]
def countPalindrones(word):
    optimal_counts = {}
    storage = [1] + [0]*len(word)
    #print(storage)
    # THIS WORkS??????
    def cPalindrones(start):
        #start at beginning, work way up to end
        for i in range(start, len(word) + 1):
            # start at index 0 up to i, see if it's a palindrome, if it is
            # store whatever is at i + what is at j
            for j in range(start, i):
                if isPalindrone(word[j:i]):
                    storage[i] += storage[j]
        #print(storage)
        # return last
        return storage[-1]
    return cPalindrones(0)
def main():
    n = int(input())
    lines = [input() for _ in range(n)]
    for word in lines:
        print(countPalindrones(word))
if __name__ == "__main__":
    main()