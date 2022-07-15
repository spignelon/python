a = input("Enter numbers: ")
a = a.split(" ")
b = [int(i) for i in a]
c = b[len(b)//2:] + b[:len(b)//2]
print(c)
