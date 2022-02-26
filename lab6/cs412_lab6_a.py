"""
lab 6 Miguel Ledesma
Algo analysis: This algorithm runs in O(n^2) time from
line 40 to 45
"""
def isPalindrone(s):
    return s == s[::-1]
def countPalindrones(word):
    optimal_counts = {}
    storage = [1] + [0]*len(word)
    #print(storage)
    # THIS WORkS??????
    def cPalindrones(start):
        for i in range(start, len(word) + 1):
            for j in range(i):
                if isPalindrone(word[j:i]):
                    storage[i] += storage[j]
        return storage[-1]
        """"
        if isPalindrone(word[start:i+1]):
            if i+1 not in optimal_counts:
                optimal_counts[i+1] = cPalindrones(i+1)
            count += optimal_counts[i+1]
        """
        #return count
        """
        DOESNT WORK FOR THE TEST BUB
        for i in range(len(word)-1, -1, -1):
            storage[i] = storage[i+1]
            for j in range(i+1, len(word) + 1):
                if len(word[i:j]) > 1:
                    if isPalindrone(word[i:j]):
                        storage[i] += 1
        
        return (storage[0] + 1)
        """
        """
        #NOT REALLY A LOOKUP ??? 
        for i in range(start, len(word)):
            if i != 0:
                storage[i] = storage[i-1]
            for j in range(i+1, len(word)):
                if isPalindrone(word[i:j]):
                    storage[i] += 1
        return storage[len(word)-1]
        """
    return cPalindrones(0)
def main():
    n = int(input())
    lines = [input() for _ in range(n)]
    for word in lines:
        print(countPalindrones(word))
if __name__ == "__main__":
    main()