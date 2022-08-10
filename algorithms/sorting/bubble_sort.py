def bubble_sort(arr: list) -> list:
    
    for i in range(len(arr) - 1):
        done = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                done = False
        if done:
            break
    return arr


# TESTING

arr = [6,5,3,1,3,4,32,0,-3]
print(bubble_sort(arr))
            

    