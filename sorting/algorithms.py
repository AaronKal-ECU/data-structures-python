import time
import random
import math
import sys

#Data Structures CSP2348, April 11th 2025
#Aaron Mark Kalaji
#Algorithm Functions without counting comparisons and completion time

def bubblesort_ob1(testarray):
    n = len(testarray)
    for i in range(n-1):
        for j in range(n-i-1):
            if testarray[j] > testarray[j+1]:
                testarray[j], testarray[j+1] = testarray[j+1], testarray[j]

def bubblesort_ob2(testarray):
    n = len(testarray)
    for i in range(n-1):
        swapped = False  #flag to track if any swaps occur
        for j in range(n-1):
            if testarray[j] > testarray[j+1]:
                testarray[j], testarray[j+1] = testarray[j+1], testarray[j]
                swapped = True  #flag when a swap occurs
        if not swapped:
            break

def bubblesort_ob3(testarray):
    n = len(testarray)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):  # observation 1
            if testarray[j] > testarray[j + 1]:
                testarray[j], testarray[j + 1] = testarray[j + 1], testarray[j]
                swapped = True
        if not swapped:  # observation 2
            break

def sinkdownsort(testarray):
    n = len(testarray)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1, i, -1):  #scan from right to left
            if testarray[j] < testarray[j - 1]:   #sink smaller element toward the front
                testarray[j], testarray[j - 1] = testarray[j - 1], testarray[j]  # Swap
                swapped = True
        if not swapped:
            break

def bdbsort(testarray):
    n = len(testarray)
    for i in range(n // 2):
        swapped = False
        for j in range(i, n - i - 1): #bubble up the largest to end of subarray
            if testarray[j] > testarray[j + 1]:
                testarray[j], testarray[j + 1] = testarray[j + 1], testarray[j]
                swapped = True
        for j in range(n - i - 2, i, -1):  #sink down the smallest to start of subarray
            if testarray[j] < testarray[j - 1]:
                testarray[j], testarray[j - 1] = testarray[j - 1], testarray[j]
                swapped = True
        if not swapped:
            break

def bubblesort(testarray):
    n = len(testarray)
    for i in range(n-1):
        for j in range(n-1):
            if testarray[j] > testarray[j+1]:
                testarray[j], testarray[j+1] = testarray[j+1], testarray[j]


def selectionsort(testarray):
    n = len(testarray)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if testarray[j] < testarray[min_idx]:
                min_idx = j
        testarray[i], testarray[min_idx] = testarray[min_idx], testarray[i]


def insertionsort(testarray):
    n = len(testarray)
    for i in range(1, n):
        key = testarray[i]
        j = i - 1
        while j >= 0 and testarray[j] > key:
            testarray[j + 1] = testarray[j]
            j -= 1
        testarray[j + 1] = key

def mergesort(testarray):
    if len(testarray) > 1:
        mid = len(testarray) // 2
        L = testarray[:mid]
        R = testarray[mid:]
        mergesort(L)
        mergesort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                testarray[k] = L[i]
                i += 1
            else:
                testarray[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            testarray[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            testarray[k] = R[j]
            j += 1
            k += 1

def quicksort(testarray, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(testarray) - 1
    if low < high:
        pi = partition(testarray, low, high)
        quicksort(testarray, low, pi - 1)
        quicksort(testarray, pi + 1, high)

def partition(testarray, low, high):
    pivot = testarray[high]
    i = low - 1
    for j in range(low, high):
        if testarray[j] <= pivot:
            i += 1
            testarray[i], testarray[j] = testarray[j], testarray[i]
    testarray[i + 1], testarray[high] = testarray[high], testarray[i + 1]
    return i + 1

def heapsort(testarray):
    n = len(testarray)
    for i in range(n // 2 - 1, -1, -1):
        heapify(testarray, n, i)
    for i in range(n - 1, 0, -1):
        testarray[i], testarray[0] = testarray[0], testarray[i]  #swap
        heapify(testarray, i, 0)

def heapify(testarray, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and testarray[largest] < testarray[left]:
        largest = left
    if right < n and testarray[largest] < testarray[right]:
        largest = right
    if largest != i:
        testarray[i], testarray[largest] = testarray[largest], testarray[i]
        heapify(testarray, n, largest)
