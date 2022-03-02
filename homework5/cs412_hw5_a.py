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
    storage = [[0 for i in range(len(part_sizes))] for j in range(len(part_sizes))]
    #print(storage)

    def part_recurs(part_index, t_remaining):
        """
            part_index = part to use
            tremaining = rocket length to assemble
        """
        
        if t_remaining == 0: return [0] * len(part_sizes)
        if part_index == -1: return [sys.maxsize] * len(part_sizes)
        best_cost = sys.maxsize
        best_list = []
        # THIS GOES BACKWARDS, THE OTHER SHOULD DO THE SAME
        for i in range(0,t_remaining//part_sizes[part_index] + 1 ):
            if part_index < 0:
                break;
            remaining = t_remaining
            storage[i][part_index] = remaining//part_sizes[part_index]
            remaining = remaining - (remaining//part_sizes[part_index] * part_sizes[part_index])
            #print("REMAINING", remaining)
            #print("Part Size: ",part_sizes[part_index])
            #print("REMAINING: ",t_remaining - 
                #(t_remaining//part_sizes[part_index] * part_sizes[part_index]))
            # GO FROM THE NEXT PART TO THE LAST PART, ADD THE PARTS REQUIRED IN (excluding current)
            for j in range(len(part_sizes)-i-2,-1, -1):
                #print(part_sizes[j])
                storage[i][j] = remaining//part_sizes[j]
                remaining = remaining - (remaining//part_sizes[j] * part_sizes[j])


            part_index -= 1
            """
            this_list = part_recurs(part_index - 1 ,
                        t_remaining - part_count * part_sizes[part_index])
            
            this_list[part_index] += part_count
            this_list_count = sum(this_list)
            if this_list_count < best_cost:
                best_cost = this_list_count
                best_list = this_list
            """
        #print(storage)
        #print(storage)
        best_cost = sys.maxsize
        best_list = []
        for i in storage:
            if sum(i) < best_cost:
                best_cost = sum(i)
                best_list = i
        return best_list
    
    return part_recurs(len(part_sizes)-1, target)
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