a = input("Enter numbers: ")
a = a.split(" ")
b = [int(i) for i in a]
b.sort()
print(b[-1])
