#bubble sort

def bubble_sort(arr):
    n = len(arr)
    #this is the number of loops we do
    for i in range(n):
        #this is the loop performing operations 
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+ 1], arr[j]
    return arr

print(bubble_sort([4,3,7, 1, 9, 6, 2, 8, 5]))

