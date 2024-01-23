def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  

def exponential_search(arr, target):
    n = len(arr)
    
    index = 1
    while index < n and arr[index] < target:
        index *= 2

    start = index // 2
    end = min(index, n - 1)
    
    result = binary_search(arr, start, end, target)

    return result

input_array = input("Enter a sorted array (comma-separated): ").split(',')
sorted_array = [int(x) for x in input_array]

target_element = int(input("Enter the target element to search for: "))

result = exponential_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the array")
