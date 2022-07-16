a = input("Enter numbers: ")
a = a.split(" ")
b = [int(i) for i in a]
c = input("Elements to remove: ")
c = c.split(" ")
d = [int(i) for i in c]
y = []
for i in range(0, len(b)):
    if b[i] not in d:
        y.append(b[i])
print(y)
