def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [20, 10, 40, 50, 90, 70, 80, 30]
target = 10

print(search(arr, target))
