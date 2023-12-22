#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:54:41 2023

@author: parisa
"""

def quicksort(arr, left, right):
    if left < right:
        # Choose the pivot as the last element and exchange it with the first element
        arr[left], arr[right] = arr[right], arr[left]
        pivot = arr[left]
        i = left + 1
        for j in range(left + 1, right + 1):
            if arr[j] < pivot:
                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        # Swap the pivot with the rightmost element of the left subarray
        arr[left], arr[i - 1] = arr[i - 1], arr[left]

        # Recursively sort the left and right subarrays
        comparisons = (right - left)  # Count comparisons for this call
        comparisons += quicksort(arr, left, i - 2)  # Sort left subarray
        comparisons += quicksort(arr, i, right)  # Sort right subarray
        return comparisons
    else:
        return 0

# Load the integers from the input file into an array
with open('QuickSort.txt', 'r') as file:
    input_array = [int(line.strip()) for line in file]

# Call the QuickSort function with the appropriate parameters
comparisons = quicksort(input_array, 0, len(input_array) - 1)

print("Total comparisons using final element as pivot:", comparisons)
