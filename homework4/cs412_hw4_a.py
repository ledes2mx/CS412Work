"""
    Homework 4: Rocket Assembly Memoized
    original Author: Kevin Molloy (Jan 2022) 
    Memoized by: Miguel Ledesma               
"""
import sys
def part_finder(part_sizes, target):
    """
        part_sizes = array of part lengths sorted in ascending order
        target = size of rocket to assemble
    """
    storage = [[None]*(target+1)]*(len(part_sizes) + 1)
    def part_recurs(part_index, t_remaining):
        """
            part_index = part to use
            tremaining = rocket length to assemble
        """
        if storage[part_index][t_remaining]:
            #print(storage[part_index][t_remaining])
            return storage[part_index][t_remaining]
        
        if t_remaining == 0: return [0] * len(part_sizes)
        if part_index == -1: return [sys.maxsize] * len(part_sizes)
        best_cost = sys.maxsize
        best_list = []
        for part_count in range(0,t_remaining//part_sizes[part_index] + 1 ):
            this_list = part_recurs(part_index - 1 ,
                            t_remaining - part_count * part_sizes[part_index])
            this_list[part_index] += part_count
            this_list_count = sum(this_list)
            if this_list_count < best_cost:
                best_cost = this_list_count
                best_list = this_list
        storage[part_index][t_remaining] = best_list
        #print(storage)
        return best_list
    
    return part_recurs(len(part_sizes)-1, target)
def main():
    part_sizes = [int(x) for x in input().split()]
    t = int(input())
    nums = 0
    i = 0
    rocket_pieces = part_finder(part_sizes, t)
    print(rocket_pieces)
    for piece in rocket_pieces:
        print(piece, "of length", part_sizes[i])
        nums += piece
        i += 1
    print(nums, "rocket sections minimum")
if __name__ == "__main__":    
    main()