def selection(arr1):
    n = len(arr1)
    for i in range(n):
        temp = i
        for j in range(i+1, n):
            if arr1[j] < arr1[temp]:
                temp = j
        arr1[i], arr1[temp] = arr1[temp], arr1[i]

def bubble(arr2):
    n=len(arr2)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr2[j]>arr2[j+1]:
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]

def insertion(arr3):
    for i in range(1, len(arr3)):
        temp = arr3[i]
        j = i - 1
        while j >= 0 and temp < arr3[j]:
            arr3[j + 1] = arr[j]
            j = j - 1
        arr3[j + 1] = temp
    return arr3

def merge(arr4, arr5, compare):
    result = []
    i, j = 0, 0
    while i < len(arr4) and j < len(arr5):
        if compare(arr4[i], arr5[j]):
            result.append(arr4[i])
            i += 1
        else:
            result.append(arr4[j])
            j += 1
    while i < len(arr4):
        result.append(arr4[i])
        i += 1
    while j < len(arr5):
        result.append(arr5[j])
        j += 1
    return result


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)


def counting_sort(l):
    nums = l
    highest = max(nums) + 1
    helper_list = [0] * highest
    s_list = []
    for i in range(len(nums)):
        value = nums[i]
        helper_list[value] += 1

    for j in range(len(helper_list)):
        s_list.append([j] * helper_list[j])

    return s_list
