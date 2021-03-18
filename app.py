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

#insertion sort
def insertion_sort(arr):
    operations = 0
    for i in range(len(arr)):
        num_we_are_on = arr[i]
        j = i - 1
        #do a check to make sure we do not go out of range
        while j >= 0 and arr[j] > num_we_are_on:
            operations += 1
            arr[j + 1] = arr[j]
            j-= 1
        j += 1
        arr[j] = num_we_are_on
    return arr, operations

print(insertion_sort([4, 6, 2, 9, 1, 8, 3, 5]))