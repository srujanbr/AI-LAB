def b_s(element):
    arr = [1, 2, 3, 4, 5]
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2

        if arr[m] == element:
            return m
        elif arr[m] < element:
            l = m + 1
        else:
            h = m - 1
    return -1
arr = [1, 2, 3, 4, 5]
target = 3
result = b_s(target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
