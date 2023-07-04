def successive_div(x, y):
    while x % y == 0:
        x = x // y
    return x
print(successive_div(6, 2))

# Function for checking if a number is ugly or not
def ugly_check(num):
    num = successive_div(num, 2)
    num = successive_div(num, 3)
    num = successive_div(num, 5)
    if num == 1:
        return True
    else:
        return False
print(ugly_check(6))
