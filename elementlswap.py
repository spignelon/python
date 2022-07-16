a = input("Enter numbers: ")
a = a.split(" ")
b = [int(i) for i in a]
print("List: {}".format(b))
z = int(input("Index value of the element you want to swap: "))
y = int(input("Index value of the element you want to swap with: "))
b[z], b[y] = b[y], b[z]
print(b)
