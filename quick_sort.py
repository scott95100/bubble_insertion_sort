#implementing quick sort function
#we will compare the quick sort with bubble sort

#bubble sort =  O(n^2)
#quick sort = O(log(n))
import random, time

sample_one = random.sample(range(1, 1000000), 100)
sample_two = random.sample(range(1, 1000000), 9999)
sample_three = random.sample(range(1, 1000000), 200000)


def quick_sort(array):
    ''' implementing quick sort algorithm'''
    #3 arrays, 1 pivot
    #Base case - consider the length of the list <= 1
    left_list = []
    mid_list = []
    right_list = []

    #base case, this is where it stops
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    for num in array:
        if num < pivot:
            left_list.append(num)
        elif num == pivot:
            mid_list.append(num)
        elif num > pivot:
            right_list.append(num)
    return quick_sort(left_list) + mid_list + quick_sort(right_list)

num_list = [88, 32, 77, 20, 1, 22]


def bubble_sort(arr):
    n = len(arr)
    #this is the number of loops we do
    for i in range(n):
        #this is the loop performing operations 
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+ 1], arr[j]
    return arr


quick_start_time= time.time()
print(quick_sort(sample_two))
quick_end_time = time.time()


bubble_start_time = time.time()
print(bubble_sort(sample_two))
bubble_end_time = time.time()


print('Quick Sort Time =>', quick_end_time - quick_start_time)
print('Bubble Sort Time =>', bubble_end_time - bubble_start_time)