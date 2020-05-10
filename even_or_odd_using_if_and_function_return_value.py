# def even_or_odd(x):
#     if x%2 == 0:
#         print("The number entered is ", x)
#         return 0
#     else:
#         print("The number entered is", x)
#         return 1


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


y = int(input("Please enter a number"))
if is_even(y):
    print("Even number")
else:
    print("Odd number")