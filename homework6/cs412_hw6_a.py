# 4:one on 6 3:done on 5 3:done on 5, 2:done on 4

from audioop import reverse


def main():
    plants = input().split(" ")
    for i in range(len(plants)):
        plants[i] = int(plants[i])
        # Add two days to each, one for the day it's planted
        # one for the ready day.
        plants[i] += 2
    plants.sort(reverse=True)
    
    minDays(plants)

def minDays(plants):
    startingMax = plants[0]
    daysToReady = 0
    growing = []
    for i in range(startingMax):
        #ADDING PLANT
        if i < len(plants):
            growing = growing + [plants[i]]
            #print("ADDING PLANT")
            if growing[i] == growing[i-1]+1:
                daysToReady += 1
        
        #GROWING PROCESS
        if len(growing) > 0:
            for j in range(len(growing)):
                if growing[j] > 0:
                    growing[j] -= 1
        #print(growing)
        daysToReady += 1
    print(daysToReady)

if __name__ == "__main__":    
    main()