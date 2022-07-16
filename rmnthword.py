a = input("Enter a sentence: ")
a = a.split()
b = input("Enter the word to remove: ")
j = 0
c = int(input("Occurance to remove:"))
for i in range(0, len(a)-1):
    if b == a[i]:
        j=j+1
        if j == c:
            a.pop(i)
print(a)
