# Miguel Ledesma

from re import search


def searcher(list, search_key, position):
    if len(list) == 1:
        if search_key != list[0]:
            print(-1)
            return -1
        print(position)
        return position
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    #print(left)
    #print( right)
    if right[0] == search_key:
        print(position + 1)
        return position+1
    if search_key >= right[0] and search_key <= right[-1]:
        #print(position + list.index(right[0]))
        searcher(right, search_key, position + list.index(right[0]))
    else:
        searcher(left,search_key, position + list.index(left[0]))

def main():
    num_list = [int(x) for x in input().split(" ")]
    key = int(input())
    searcher(num_list, key, 0)

if __name__ == "__main__":
    main()
