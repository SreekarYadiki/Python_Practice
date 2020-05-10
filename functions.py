
def palindrome():
    a = input("Enter a string:")
    if a[:] == a[::-1]:
        print(a, "is palindrome")
    else:
        print(a, "is not palindrome")


def add():
    b = int(input("Enter a number"))
    c = int(input("Enter a number"))
    print(b+c)


def fun1():
    print("Invoking palindrome functionality")
    palindrome()
    print("Invoking add")
    add()


for item in range(3):
    fun1()
