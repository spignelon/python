a = int(input("Enter a number: "))
b = 1
for i in range(1,a+1):
    b = i*b
print("Factorial is:",b)
x, y, b = 0, 1, 0
print("Fibonacci series:", x , y, end=" ")
for i in range(a-1):
    b = x + y
    x, y = y, b
    print(b, end=" ")