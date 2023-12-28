
import math


def f4(n):
    """
    Calculates and returns the log base 2 of a given number. This is for use with Kleinberg/Tardos
    Chapter 2 exercises.
    :param n: number on which to calculate log base 2
    :return: log base 2 of the given number
    """
    ret = math.log(n, 2)
    return ret

def f5(n):
    """
    Calculates 2 to the power of the square root of log base 2 of a given number, n.
    This is for use with Kleinberg/Tardos Chapter 2 exercises.
    :param n: number to plug into the function
    :return: result
    """
    ret = 2**(math.sqrt(math.log(n, 2)))
    return ret

def compare_f4_and_f5():
    print("f4 ______|____f5______")
    print(f4(8), "     | ", f5(8))
    print(f4(16), "     | ", f5(16))
    print(f4(256), "     | ", f5(256))
    print(f4(2**16), "    | ", f5(2**16))
    print(f4(2**20), "    | ", f5(2**20))
    print(f4(2**30), "    | ", f5(2**30))
    print(f4(2**40), "    | ", f5(2**40))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    compare_f4_and_f5()






