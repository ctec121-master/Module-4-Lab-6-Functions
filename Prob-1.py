# Prob-1.py

def function1(a, b):
    if a < 10:
        return -2
    elif a > 10:
        return 2
    elif b < 5:
        return -1
    elif b > 5:
        return 1
    else:
        return 0


def unitTest():
    print("Running unit tests\n")
    print("Test 1: a = 0, b = 0, expected value: -2, actual value:", function1(0, 0))
    # your code below here

    print()


if __name__ == "__main__":
    unitTest()        