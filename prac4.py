# NAME - HITEN BORKAR
# BATCH - A5 B1
# ROLL NO: 15

def max_subarray_sum(arr, low, high, constraint):
    if low == high:
        if arr[low] <= constraint:
            return arr[low], [arr[low]]
        else:
            return float('-inf'), None

    mid = (low + high) // 2
    left_sum, left_subarray = max_subarray_sum(arr, low, mid, constraint)
    right_sum, right_subarray = max_subarray_sum(arr, mid + 1, high, constraint)
    cross_sum, cross_subarray = max_crossing_sum(arr, low, mid, high, constraint)

    max_val = max(left_sum, right_sum, cross_sum)
    if max_val == left_sum:
        return left_sum, left_subarray
    elif max_val == right_sum:
        return right_sum, right_subarray
    else:
        return cross_sum, cross_subarray


def max_crossing_sum(arr, low, mid, high, constraint):
    left_sum = float('-inf')
    sum_ = 0
    best_left = None
    for i in range(mid, low - 1, -1):
        sum_ += arr[i]
        if sum_ <= constraint and sum_ > left_sum:
            left_sum = sum_
            best_left = arr[i:mid + 1]

    right_sum = float('-inf')
    sum_ = 0
    best_right = None
    for j in range(mid + 1, high + 1):
        sum_ += arr[j]
        if sum_ <= constraint and sum_ > right_sum:
            right_sum = sum_
            best_right = arr[mid + 1:j + 1]

    if left_sum == float('-inf') and right_sum == float('-inf'):
        return float('-inf'), None
    elif left_sum == float('-inf'):
        return right_sum, best_right
    elif right_sum == float('-inf'):
        return left_sum, best_left

    cross = left_sum + right_sum
    if cross <= constraint:
        return cross, best_left + best_right
    else:
        if left_sum >= right_sum:
            return left_sum, best_left
        else:
            return right_sum, best_right


def find_max_subarray(arr, constraint):
    if not arr or constraint <= 0:
        return None, 0
    max_sum, subarray = max_subarray_sum(arr, 0, len(arr) - 1, constraint)
    if max_sum == float('-inf'):
        return None, 0
    return subarray, max_sum


test_cases = [([2, 1, 3, 4], 5),
              ([2, 2, 2, 2], 4),
              ([1, 5, 2, 3], 5),
              ([6, 7, 8], 5),
              ([1, 2, 3, 2, 1], 5),
              ([1, 1, 1, 1, 1], 4),
              ([4, 2, 3, 1], 5),
              ([], 10),
              ([1, 2, 3], 0),
              (list(range(1, 100001)), 10**9),
]

for i, (arr, c) in enumerate(test_cases, 1):
    subarray, s = find_max_subarray(arr, c)
    print(f"Test-{i}: Best Subarray = {subarray}, Sum = {s}")



# OUTPUT ----
# Test-1: Best Subarray = [4], Sum = 4
# Test-2: Best Subarray = [2, 2], Sum = 4
# Test-3: Best Subarray = [5], Sum = 5
# Test-4: Best Subarray = None, Sum = 0
# Test-5: Best Subarray = [2, 3], Sum = 5
# Test-6: Best Subarray = [1, 1, 1], Sum = 3
# Test-7: Best Subarray = [4], Sum = 4
# Test-8: Best Subarray = None, Sum = 0
# Test-9: Best Subarray = None, Sum = 0
# Test-10: Best Subarray = [75001, 75002, 75003, 75004, 75005,....