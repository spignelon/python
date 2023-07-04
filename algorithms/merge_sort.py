def sortArray(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = sortArray(A[:middle])
    right = sortArray(A[middle:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

A = [-5, -23, 5, 0, 23, -6, 23, 67]
print(sortArray(A))
