def quick_sort(arr: list) -> list:
    _quick_sort(arr, 0, len(arr) - 1)    
    
def _quick_sort(arr: list, l:int, h:int):
    if l < h:
        pi = partition(arr, l, h)
        _quick_sort(arr, l, pi - 1)
        _quick_sort(arr, pi + 1, h)
    
def partition(arr: list, l:int, h:int):
    i = l
    pivot = arr[h]
    
    for j in range(l, h):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[h], arr[i] = arr[i], arr[h]
    return i


# TESTING
a = [3,5,0,-1,14,-300]
quick_sort(a)
print(a)