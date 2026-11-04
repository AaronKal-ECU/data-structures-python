import time
import random
import math
import sys


# Data Structures CSP2348, April 11th 2025
# Aaron Mark Kalaji
# Functions File

def bubblesort(arr, n):
    comparisons = 0
    for i in range(n - 1):
        for j in range(n - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

def bubblesort_ob1(arr, n):
    comparisons = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

def bubblesort_ob2(arr, n):
    comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

def bubblesort_ob3(arr, n):
    comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

def sinkdownsort(arr, n):
    comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1, i, -1):
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

def bdbsort(arr, n):
    comparisons = 0
    for i in range(n // 2):
        swapped = False
        for j in range(i, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        for j in range(n - i - 2, i, -1):
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

def selectionsort(arr, n):
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

def insertionsort(arr, n):
    comparisons = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

merge_comparisons = 0
quick_comparisons = 0
heap_comparisons = 0

def mergesort(arr, n):
    global merge_comparisons
    merge_comparisons = 0
    _mergesort(arr, 0, n - 1)
    return merge_comparisons

def _mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        _mergesort(arr, left, mid)
        _mergesort(arr, mid + 1, right)
        _merge(arr, left, mid, right)

def _merge(arr, left, mid, right):
    global merge_comparisons
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        merge_comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def quicksort(arr, n):
    global quick_comparisons
    quick_comparisons = 0
    _quicksort(arr, 0, n - 1)
    return quick_comparisons

def _quicksort(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quicksort(arr, low, pi - 1)
        _quicksort(arr, pi + 1, high)

def _partition(arr, low, high):
    global quick_comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        quick_comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapsort(arr, n):
    global heap_comparisons
    heap_comparisons = 0
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    return heap_comparisons

def _heapify(arr, n, i):
    global heap_comparisons
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n:
        heap_comparisons += 1
        if arr[largest] < arr[left]:
            largest = left
    if right < n:
        heap_comparisons += 1
        if arr[largest] < arr[right]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def generate_random_array(n):
    return [random.randint(1, 10000) for _ in range(n)]

def test_sorting_algorithm(algorithm, n, runs=1):
    if runs <= 0:
        runs = 1
    elif runs > 10:
        runs = 10
    total_time = 0
    total_comparisons = 0

    if runs == 1:
        arr = generate_random_array(n)
        original_arr = arr.copy()

        print(f"\nOriginal array: {original_arr}")
        start_time = time.time()
        comparisons = algorithm(arr, n)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Sorted array: {arr}")
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Number of comparisons: {comparisons}")

        is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        print(f"Is sorted correctly: {is_sorted}")

        return execution_time, comparisons, is_sorted

    print(f"\nRunning {algorithm.__name__} {runs} times with array size {n}...")
    for i in range(runs):
        arr = generate_random_array(n)

        start_time = time.time()
        comparisons = algorithm(arr, n)
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time
        total_comparisons += comparisons
        is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        if not is_sorted:
            print(f"Warning: Run {i + 1} did not sort correctly!")

    avg_time = total_time / runs
    avg_comparisons = total_comparisons // runs

    print(f"\nResults after {runs} runs:")
    print(f"Average execution time: {avg_time:.6f} seconds")
    print(f"Average number of comparisons: {avg_comparisons}")
    return avg_time, avg_comparisons, True

def test_all_algorithms(n, runs=1):
    if runs <= 0:
        runs = 1
    elif runs > 10:
        runs = 10

    algorithms = [
        ("Selection Sort", selectionsort),
        ("Insertion Sort", insertionsort),
        ("Merge Sort", mergesort),
        ("Quick Sort", quicksort),
        ("Heap Sort", heapsort),
        ("Bubble Sort", bubblesort),
        ("Bubble Sort (Obs1)", bubblesort_ob1),
        ("Bubble Sort (Obs2)", bubblesort_ob2),
        ("Bubble Sort (Obs3)", bubblesort_ob3),
        ("Sink-down Sort", sinkdownsort),
        ("BDB Sort", bdbsort)
    ]

    if runs == 1:
        original_arr = generate_random_array(n)
        print(f"\nTesting all algorithms with array size: {n}")
        print(f"Original array: {original_arr}")

        results = []
        for name, algorithm in algorithms:
            arr = original_arr.copy()
            start_time = time.time()
            comparisons = algorithm(arr, n)
            end_time = time.time()
            execution_time = end_time - start_time
            is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
            results.append((name, execution_time, comparisons, is_sorted))

    else:
        print(f"\nTesting all algorithms with array size: {n}, {runs} runs each")

        results = []
        for name, algorithm in algorithms:
            total_time = 0
            total_comparisons = 0
            all_sorted = True
            for i in range(runs):
                arr = generate_random_array(n)
                start_time = time.time()
                comparisons = algorithm(arr, n)
                end_time = time.time()
                execution_time = end_time - start_time
                total_time += execution_time
                total_comparisons += comparisons
                is_sorted = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
                if not is_sorted:
                    all_sorted = False

            avg_time = total_time / runs
            avg_comparisons = total_comparisons // runs  # Integer division for comparison count
            results.append((name, avg_time, avg_comparisons, all_sorted))

    if runs == 1:
        print("\n" + "=" * 80)
        print(f"{'Algorithm':<20} | {'Time (seconds)':<15} | {'Comparisons':<15} | {'Sorted Correctly':<15}")
    else:
        print("\n" + "=" * 80)
        print(f"{'Algorithm':<20} | {'Avg Time (s)':<15} | {'Avg Comparisons':<15} | {'All Sorted':<15}")
    print("-" * 80)
    for name, time_taken, comparisons, is_sorted in results:
        print(f"{name:<20} | {time_taken:<15.6f} | {comparisons:<15} | {is_sorted:<15}")
    print("=" * 80)

    fastest_by_time = min(results, key=lambda x: x[1])
    fewest_comparisons = min(results, key=lambda x: x[2])

    if runs == 1:
        print(f"\nFastest algorithm by time: {fastest_by_time[0]} ({fastest_by_time[1]:.6f} seconds)")
        print(f"Algorithm with fewest comparisons: {fewest_comparisons[0]} ({fewest_comparisons[2]} comparisons)")
    else:
        print(f"\nFastest algorithm by average time: {fastest_by_time[0]} ({fastest_by_time[1]:.6f} seconds)")
        print(
            f"Algorithm with fewest average comparisons: {fewest_comparisons[0]} ({fewest_comparisons[2]} comparisons)")

    return results
