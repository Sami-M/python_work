"""
Created by Sami on 12/6/2016
"""

def merge_sort(unsorted_list):
    print("sorting", unsorted_list)
    if(len(unsorted_list) != 1):
        middle = len(unsorted_list) // 2
        leftArray = unsorted_list[0:middle]
        rightArray = unsorted_list[middle:]
        merge_sort(leftArray)
        merge_sort(rightArray)
        i = 0
        j = 0
        k = 0
        print('merging ', unsorted_list)
        while (i < len(leftArray) and j < len(rightArray)):
            if(leftArray[i] < rightArray[j]):
                unsorted_list[k] = leftArray[i]
                i = i + 1
            else:
                unsorted_list[k] = rightArray[j]
                j = j + 1
            k = k + 1
        while (i < len(leftArray)):
            unsorted_list[k] = leftArray[i]
            i = i + 1
            k = k + 1
        while (j < len(rightArray)):
            unsorted_list[k] = rightArray[j]
            j = j + 1
            k = k + 1