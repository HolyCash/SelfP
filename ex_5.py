x = input("Put your number here please:")
def func1(x):
    try:
        return float(x)
    except (ValueError):
        print("Enter the number please.")
print(func1(x))
