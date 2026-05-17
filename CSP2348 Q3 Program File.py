import Functions as sa
import time
import random
import math
import sys


# Data Structures CSP2348, April 11th 2025
# Aaron KALAJI 10670705
# Program File

def clear_screen():
    print("\n" * 50)

def main_menu():
    while True:
        clear_screen()
        print("\n===== SORTING ALGORITHMS =====")
        print("1. Test an individual sorting algorithm")
        print("2. Test all sorting algorithms")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            individual_algorithm_menu()
        elif choice == '2':
            test_all_algorithms_menu()
        elif choice == '3':
            print("\nExiting.")
            break
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)

def test_all_algorithms_menu():
    clear_screen()
    print("\n===== TEST ALL SORTING ALGORITHMS =====")
    try:
        n = int(input("\nEnter the size of the array (n > 0): "))
        if n <= 0:
            raise ValueError("Array size must be positive")
    except ValueError as e:
        print(f"\nInvalid input: {e}. Please try again.")
        time.sleep(1.5)
        return
    try:
        runs = int(input("\nEnter the number of runs (1-10): "))
        if runs < 1:
            print("\nNumber of runs must be at least 1. Setting to 1.")
            runs = 1
        elif runs > 10:
            print("\nMaximum number of runs is 10. Setting to 10.")
            runs = 10
    except ValueError as e:
        print(f"\nInvalid input: {e}. Using default of 1 run.")
        runs = 1
        time.sleep(1.5)
    sa.test_all_algorithms(n, runs)
    print("\n1. Return to main menu")
    print("2. Exit program")
    after_test_choice = input("\nEnter your choice (1-2): ")
    if after_test_choice == '1':
        return
    elif after_test_choice == '2':
        print("\nExiting.")
        sys.exit(0)
    else:
        print("\nInvalid choice. Returning to main menu.")
        time.sleep(1.5)

def individual_algorithm_menu():
    while True:
        clear_screen()
        print("\n===== TEST SORTING ALGORITHM =====")
        print("1. Test selection sort algorithm")
        print("2. Test insertion sort algorithm")
        print("3. Test merge sort algorithm")
        print("4. Test quick sort algorithm")
        print("5. Test heap sort algorithm")
        print("6. Test bubble sort algorithm")
        print("7. Test Sink-down sort algorithm")
        print("8. Test BDB sort algorithm")
        print("9. Return to main menu")
        choice = input("\nEnter your choice (1-9): ")
        if choice == '9':
            break
        if choice == '6':
            bubble_sort_menu()
            continue
        try:
            n = int(input("\nEnter the size of the array (n > 0): "))
            if n <= 0:
                raise ValueError("Array size must be positive")
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please try again.")
            time.sleep(1.5)
            continue
        try:
            runs = int(input("\nEnter the number of runs (1-10): "))
            if runs < 1:
                print("\nNumber of runs must be at least 1. Setting to 1.")
                runs = 1
            elif runs > 10:
                print("\nMaximum number of runs is 10. Setting to 10.")
                runs = 10
        except ValueError as e:
            print(f"\nInvalid input: {e}. Using default of 1 run.")
            runs = 1
            time.sleep(1.5)
        if choice == '1':
            sa.test_sorting_algorithm(sa.selectionsort, n, runs)
        elif choice == '2':
            sa.test_sorting_algorithm(sa.insertionsort, n, runs)
        elif choice == '3':
            sa.test_sorting_algorithm(sa.mergesort, n, runs)
        elif choice == '4':
            sa.test_sorting_algorithm(sa.quicksort, n, runs)
        elif choice == '5':
            sa.test_sorting_algorithm(sa.heapsort, n, runs)
        elif choice == '7':
            sa.test_sorting_algorithm(sa.sinkdownsort, n, runs)
        elif choice == '8':
            sa.test_sorting_algorithm(sa.bdbsort, n, runs)
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)
            continue

        print("\n1. Return to main menu")
        print("2. Exit program")
        after_test_choice = input("\nEnter your choice (1-2): ")
        if after_test_choice == '1':
            break
        elif after_test_choice == '2':
            print("\nExiting.")
            sys.exit(0)
        else:
            print("\nInvalid choice. Returning to algorithm menu.")
            time.sleep(1.5)

def bubble_sort_menu():
    while True:
        clear_screen()
        print("\n===== BUBBLE-SORT ALGORITHMS =====")
        print("1. Test bubble sort")
        print("2. Test Obs1-bubble sort")
        print("3. Test Obs2-bubble sort")
        print("4. Test Obs3-bubble sort")
        print("5. Return to algorithm menu")
        choice = input("\nEnter your choice (1-5): ")
        if choice == '5':
            break
        try:
            n = int(input("\nEnter the size of the array (n > 0): "))
            if n <= 0:
                raise ValueError("Array size must be positive")
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please try again.")
            time.sleep(1.5)
            continue
        try:
            runs = int(input("\nEnter the number of runs (1-10): "))
            if runs < 1:
                print("\nNumber of runs must be at least 1. Setting to 1.")
                runs = 1
            elif runs > 10:
                print("\nMaximum number of runs is 10. Setting to 10.")
                runs = 10
        except ValueError as e:
            print(f"\nInvalid input: {e}. Using default of 1 run.")
            runs = 1
            time.sleep(1.5)
        if choice == '1':
            sa.test_sorting_algorithm(sa.bubblesort, n, runs)
        elif choice == '2':
            sa.test_sorting_algorithm(sa.bubblesort_ob1, n, runs)
        elif choice == '3':
            sa.test_sorting_algorithm(sa.bubblesort_ob2, n, runs)
        elif choice == '4':
            sa.test_sorting_algorithm(sa.bubblesort_ob3, n, runs)
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)
            continue

        print("\n1. Return to main menu")
        print("2. Exit program")
        after_test_choice = input("\nEnter your choice (1-2): ")
        if after_test_choice == '1':
            return
        elif after_test_choice == '2':
            print("\nExiting.")
            sys.exit(0)
        else:
            print("\nInvalid choice. Returning to bubble sort menu.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
