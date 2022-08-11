def insertion_sort(arr: list) -> list:
    
    for i in range(1, len(arr) - 1):
        
        # range(start, stop, step)
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


#TESTING
print(insertion_sort([1,5,6,3,-1,-3,0,14]))
            