"""
    Homework 5: Rocket Assembly Memoized
    original Author: Kevin Molloy (Jan 2022) 
    Dynamically Implemented by: Miguel Ledesma               
"""
import sys
def part_finder(part_sizes, target):
    """
        part_sizes = array of part lengths sorted in ascending order
        target = size of rocket to assemble
    """
    #storage = [None for i in range(len(part_sizes)+1)]
    # FILLED WITH THE WORST CASE AT THE BEGINNING SINCE 1 IS ALWAYS PRESENT
    storage = [i for i in range(target+1)]
    # LIST OF LISTS FILLED WITH 0S TO PUT PARTS USED IN THE PROPPER PLACE
    store = [[0 for i in range(len(part_sizes))] for j in range(target+1)]
    #print(storage)
    #print(store)

    def part_recurs(part_index, t_remaining):
        """
            part_index = part to use
            tremaining = rocket length to assemble
        """
        
        if t_remaining == 0: return [0] * len(part_sizes)
        if part_index == -1: return [sys.maxsize] * len(part_sizes)

        for i in range(1, len(storage)):
            # NEED TO HAVE SOMETHING HERE TO REFREENCE IT LATER, PART BEING SOMETHING SPECIFIC DOESN'T REALLY MATTER HERE
            part = 0
            # GO THROUGH EVERY PART IN EACH LIST OF LIST
            for currPart in part_sizes:
                # TAKES THE MINIMUM AND PUTS IT INTO WHERE I IS
                if storage[i-currPart] < storage[i]:
                    storage[i] = storage[i-currPart] + 1
                    part = currPart
            # THIS GETS THE LIST BEING STORED AT i, only grabbing store[i-part] grabs something weird and throws it all off
            store[i] = store[i-part][:]
            #print(store[i])
            store[i][part_sizes.index(part)] += 1
        #print(store[-1])



        # THIS GOES BACKWARDS, THE OTHER SHOULD DO THE SAME
        """
        for i in range(0,t_remaining//part_sizes[part_index] + 1 ):
            if part_index < 0:
                break;
            remaining = t_remaining
            storage[i][part_index] = remaining//part_sizes[part_index]
            remaining = remaining - (remaining//part_sizes[part_index] * part_sizes[part_index])
            # GO FROM THE NEXT PART TO THE LAST PART, ADD THE PARTS REQUIRED IN (excluding current)
            for j in range(len(part_sizes)-i-2,-1, -1):
                storage[i][j] = remaining//part_sizes[j]
                remaining = remaining - (remaining//part_sizes[j] * part_sizes[j])
        best_cost = sys.maxsize
        best_list = []
        for i in storage:
            if sum(i) < best_cost and sum(i) != 0:
                best_cost = sum(i)
                best_list = i
        """
        return store[-1]
    
    return part_recurs(0, target)
def main():
    part_sizes = [int(x) for x in input().split()]
    t = int(input())
    nums = 0
    i = 0
    rocket_pieces = part_finder(part_sizes, t)
    #print(rocket_pieces)
    for piece in rocket_pieces:
        print(piece, "of length", part_sizes[i])
        nums += piece
        i += 1
    print(nums, "rocket sections minimum")
if __name__ == "__main__":    
    main()