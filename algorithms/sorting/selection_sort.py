def selection_sort(arr: list) -> list:
    
    length = len(arr) - 1
    
    for i in range(length):
        minidx = i
        
        for j in range(i + 1, length):
    
            if arr[minidx] > arr[j]:
                minidx = j
    
        if minidx != i:
            arr[minidx], arr[i] = arr[i], arr[minidx]
    
    return arr


#TESTING
a = [1,5,2,13,-42,0,12]
selection_sort(a)
print(a)