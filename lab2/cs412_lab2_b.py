# check which elements are less than the index
# Think about merge sort, cut list in half COUNT INVERSIONS

"""
   MergeSort
   coded by Bowers from Jeff Erickson's pseudocode
"""
def mergesort(list):
    if len(list) > 1:
        # Get the mid point
        m = len(list) // 2
        # Get the left and right halves
        left, right = list[:m], list[m:]
        # sort the left and right halves
        mergesort(left)
        mergesort(right)
        # Copy the sorted left and right halves back to A. 
        for i in range(m):
            list[i] = left[i]
        for j in range(m, len(list)):
            list[j] = right[j - m]
        
        # Run the merge operation on A
        merge(list,m)
        
def merge(list, m):
    i, j = 0, m
    n = len(list)
    temp = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            temp[k] = list[i]
            i += 1
        elif i >= m:
            temp[k] = list[j]
            j += 1
        elif list[i] <= list[j]:
            temp[k] = list[i]
            i += 1
        else:
            temp[k] = list[j]
            j += 1
    for k in range(n):
        list[k] = temp[k]
def main():
    list = [int(x) for x in input().split(" ")]
    mergesort(list)
if __name__ == "__main__":
    main()