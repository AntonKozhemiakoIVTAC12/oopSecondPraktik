'''n = 10
a = [0]*n
from random import randint
for i in range(n):
    a[i] = randint(1,20)
print(a)
min = a[0]
for i in range(1,n):
    if a[i] < min:
        min = a[i]
print(min)'''
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

random_list_of_nums = [22, 5, 2, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
print(random_list_of_nums[0])

'''def binary_search(random_list_of_nums, start_element, key):
    end_element = len(sequence) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if sequence[middle_element] == key:
            return middle_element
        elif sequence[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1'''
