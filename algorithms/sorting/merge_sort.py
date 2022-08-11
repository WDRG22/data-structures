from turtle import right


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    mid_idx = len(arr) // 2     # Get middle index
    left_arr = arr[:mid_idx]    # Split array in half
    right_arr = arr[mid_idx:]
    
    left_sorted = merge_sort(left_arr)      # Recursively split arrays in half 
    right_sorted = merge_sort(right_arr)
    
    return merge(left_sorted, right_sorted) # Sort and merge arrays
    
def merge(left_arr: list, right_arr: list):
    result = []
    
    # While both arrays contain elements, append smaller of 0th element to result array
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            result.append(left_arr.pop(0))
        else:
            result.append(right_arr.pop(0))
            
    # Append remaining elements of whichever array still contains elements to result
    if left_arr:
        result += left_arr
        
    if right_arr:
        result += right_arr
        
    return result

a = [356, 746, 264, -569, 949, 895, 125, 455]
b = [787, 677, 391, -318, 543, 0, 180, 113, 795, 19, 202, 534, 201, -370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
c = [860, 380, 151, -585, 743, 0, 147, 820, 439, 865, 924, 387]

a2 = merge_sort(a)
b2 = merge_sort(b)
c2 = merge_sort(c)

print(a2)
print(b2)
print(c2)