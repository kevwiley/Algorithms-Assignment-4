"""
Sorting Assignment Starter Code
Implement five sorting algorithms and benchmark their performance.
"""

import json
import time
import random
import tracemalloc


# ============================================================================
# PART 1: SORTING IMPLEMENTATIONS
# ============================================================================

def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm.
    
    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they're in the wrong order.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        bubble_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement bubble sort
    # Hint: Use nested loops - outer loop for passes, inner loop for comparisons
    # Hint: Compare adjacent elements and swap if left > right
    
    #loops through items, can also check if working with dictionary
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):

            #checks if the items are dictionaries and compares prices
            if isinstance(arr[j], dict):
                if arr[j]["price"] > arr[j + 1]["price"]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            #compares item values normally
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """
    Sort array using selection sort algorithm.
    
    Selection sort divides the list into sorted and unsorted regions, repeatedly
    selecting the minimum element from unsorted region and moving it to sorted region.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        selection_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement selection sort
    # Hint: Find minimum element in unsorted portion, swap it with first unsorted element
    
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            #checks if items are in dictionaries and compares prices
            if isinstance(arr[j], dict):
                if arr[j]["price"] < arr[min_index]["price"]:
                    min_index = j
            #compares values
            else:
                if arr[j] < arr[min_index]:
                    min_index = j

        #swaps the smallest item into position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm.
    
    Insertion sort builds the final sorted array one item at a time, inserting
    each element into its proper position in the already-sorted portion.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        insertion_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement insertion sort
    # Hint: Start from second element, insert it into correct position in sorted portion
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        #gets price if dictionary
        if isinstance(key, dict):
            key_value = key["price"]
        else:
            key_value = key

        #moves larger items right
        while j >= 0:
            #gets value of item being compared
            if isinstance(arr[j], dict):
                current_value = arr[j]["price"]
            else:
                current_value = arr[j]

            if current_value > key_value:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        #puts key into correct position
        arr[j + 1] = key

    return arr


def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that divides the array into halves,
    recursively sorts them, and then merges the sorted halves.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        merge_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement merge sort
    # Hint: Base case - if array has 1 or 0 elements, it's already sorted
    # Hint: Recursive case - split array in half, sort each half, merge sorted halves
    # Hint: You'll need a helper function to merge two sorted arrays
    
    #makes sure the list has more than one element
    if len(arr) > 1:
        m = len(arr) // 2

        #gets left and right side of data
        l = arr[:m]
        r = arr[m:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):

            #gets the values to compare
            if isinstance(l[i], dict):
                left_value = l[i]["price"]
            else:
                left_value = l[i]

            if isinstance(r[j], dict):
                right_value = r[j]["price"]
            else:
                right_value = r[j]

            #equal items kept in original order
            if left_value <= right_value:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        #remaining elements are put into array
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return arr

# ============================================================================
# PART 2: STABILITY DEMONSTRATION
# ============================================================================

def demonstrate_stability():
    """
    Demonstrate which sorting algorithms are stable by sorting products by price.
    
    Creates a list of product dictionaries with prices and original order.
    Sorts by price and checks if products with same price maintain original order.
    
    Returns:
        dict: Results showing which algorithms preserved order for equal elements
    """
    # Sample products with duplicate prices
    products = [
        {"name": "Widget A", "price": 1999, "original_position": 0},
        {"name": "Gadget B", "price": 999, "original_position": 1},
        {"name": "Widget C", "price": 1999, "original_position": 2},
        {"name": "Tool D", "price": 999, "original_position": 3},
        {"name": "Widget E", "price": 1999, "original_position": 4},
    ]
    
    # TODO: Sort products by price using each algorithm
    # Hint: You'll need to modify your sorting functions to work with dictionaries
    # Hint: Or extract prices, sort them, and check if stable algorithms maintain original order
    # Hint: For stable sort: items with price 999 should stay in order (B before D)
    # Hint: For stable sort: items with price 1999 should stay in order (A before C before E)
    # TODO: Test each algorithm and update results dictionary with "Stable" or "Unstable"

    #makes copies so each algorithm gets original list
    bubble_products = products.copy()
    selection_products = products.copy()
    insertion_products = products.copy()
    merge_products = products.copy()

    #calls sorting functions
    bubble_sort(bubble_products)
    selection_sort(selection_products)
    insertion_sort(insertion_products)
    merge_sort(merge_products)

    #sorts the products using each algorithm
    bubble_sort(bubble_products)
    selection_sort(selection_products)
    insertion_sort(insertion_products)
    merge_sort(merge_products)

    #store the sorted results
    sorted_products = {
        "bubble_sort": bubble_products,
        "selection_sort": selection_products,
        "insertion_sort": insertion_products,
        "merge_sort": merge_products
    }

    results = {}

    #checks each sorting algorithm
    for algorithm, products_sorted in sorted_products.items():

        stable = True
        #check neighboring products for same price and original position
        for i in range(len(products_sorted) - 1):

            if products_sorted[i]["price"] == products_sorted[i + 1]["price"]:
                if products_sorted[i]["original_position"] > products_sorted[i + 1]["original_position"]:
                    stable = False
                    break

        #save the result to results dictionary
        if stable:
            results[algorithm] = "Stable"
        else:
            results[algorithm] = "Not Stable"

    return results
   
# ============================================================================
# PART 3: PERFORMANCE BENCHMARKING
# ============================================================================

def load_dataset(filename):
    """Load a dataset from JSON file."""
    with open(f"datasets/{filename}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_sorting_correctness():
    """Test that sorting functions work correctly on small test cases."""
    print("="*70)
    print("TESTING SORTING CORRECTNESS")
    print("="*70 + "\n")
    
    test_cases = load_test_cases()
    
    test_names = ["small_random", "small_sorted", "small_reverse", "small_duplicates"]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for test_name in test_names:
        print(f"Test: {test_name}")
        print(f"  Input:    {test_cases[test_name]}")
        print(f"  Expected: {test_cases['expected_sorted'][test_name]}")
        print()
        
        for algo_name, algo_func in algorithms.items():
            try:
                result = algo_func(test_cases[test_name].copy())
                expected = test_cases['expected_sorted'][test_name]
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"    {algo_name:20s}: {result} {status}")
            except Exception as e:
                print(f"    {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def benchmark_algorithm(sort_func, data):
    """
    Benchmark a sorting algorithm on given data.
    
    Args:
        sort_func: The sorting function to test
        data: The dataset to sort (will be copied so original isn't modified)
    
    Returns:
        tuple: (execution_time_ms, peak_memory_kb)
    """
    # Copy data so we don't modify original
    data_copy = data.copy()
    
    # Start memory tracking
    tracemalloc.start()
    
    # Measure execution time
    start_time = time.perf_counter()
    sort_func(data_copy)
    end_time = time.perf_counter()
    
    # Get peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak / 1024
    
    return execution_time_ms, peak_memory_kb


def benchmark_all_datasets():
    """Benchmark all sorting algorithms on all datasets."""
    print("\n" + "="*70)
    print("BENCHMARKING SORTING ALGORITHMS")
    print("="*70 + "\n")
    
    datasets = {
        "orders.json": ("Order Processing Queue", 50000, 5000),
        "products.json": ("Product Catalog", 100000, 5000),
        "inventory.json": ("Inventory Reconciliation", 25000, 5000),
        "activity_log.json": ("Customer Activity Log", 75000, 5000)
    }
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for filename, (description, full_size, sample_size) in datasets.items():
        print(f"Dataset: {description} ({sample_size:,} element sample)")
        print("-" * 70)
        
        data = load_dataset(filename)
        # Use first sample_size elements for fair comparison
        data_sample = data[:sample_size]
        
        for algo_name, algo_func in algorithms.items():
            try:
                exec_time, memory = benchmark_algorithm(algo_func, data_sample)
                print(f"  {algo_name:20s}: {exec_time:8.2f} ms | {memory:8.2f} KB")
            except Exception as e:
                print(f"  {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def analyze_stability():
    """Test and display which algorithms are stable."""
    print("="*70)
    print("STABILITY ANALYSIS")
    print("="*70 + "\n")
    
    print("Testing which algorithms preserve order of equal elements...\n")
    
    results = demonstrate_stability()
    
    for algo_name, stability in results.items():
        print(f"  {algo_name:20s}: {stability}")
    
    print()


if __name__ == "__main__":
    print("SORTING ASSIGNMENT - STARTER CODE")
    print("Implement the sorting functions above, then run tests.\n")
    
    # Uncomment these as you complete each part:
    
    #test_sorting_correctness() #Assignment says to uses test_small for this instead of this function

    benchmark_all_datasets()
    analyze_stability()
    
    print("\n⚠ Uncomment the test functions in the main block to run benchmarks!")