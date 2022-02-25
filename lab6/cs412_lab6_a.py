"""
lab 6 Miguel Ledesma
"""
def isPalindrone(s):
    return s == s[::-1]
def countPalindrones(word):
    optimal_counts = {}
    def cPalindrones(start):
        """
        count = 0
        if start == len(word):
            return 1
        for i in range(start, len(word)):
            if isPalindrone(word[start:i+1]):
                if i+1 not in optimal_counts:
                    optimal_counts[i+1] = cPalindrones(i+1)
                count += optimal_counts[i+1]
        """
        #return count
        storage = [0] * (len(word)+1)
        #print(storage)
        #check if value is not in dictionary, if not, add it to dictionary
        if 1 >= len(word):
            return 1
        #for i in range(start, len(word)+1):
        for i in range(-1, -(len(word)+1), -1):
            #print(i)
            for j in range(len(word)+i, len(word)):
                #print(word[i:j+1])
                if len(word[i:j+1]) == 1:
                    if word[i:j+1] not in optimal_counts.values():
                        #print("NOT IN YET")
                    #print(word[i:j+1])
                        optimal_counts[j] = word[i:j+1]
                        storage[j] += storage[j+1] + 1
                        #print(storage)

                    #print(j)
                    else:
                        storage[j] = storage[j+1]
                        #print(storage)
                elif isPalindrone(word[i:j+1]):
                    #print("IS PALINDROME")
                    storage[i-1] += 1
            #print(word[i:])
        #print(len(storage))
        if len(storage)-1 == len(optimal_counts):
            storage[0] = storage[0] - (len(optimal_counts) -1) 
        return storage[0]
    return cPalindrones(0)
def main():
    n = int(input())
    lines = [input() for _ in range(n)]
    for word in lines:
        print(countPalindrones(word))
if __name__ == "__main__":
    main()