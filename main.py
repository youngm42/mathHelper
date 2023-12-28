
import math
import matplotlib.pyplot as plt

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

    x = [8, 16, 256, 2**16, 2**20, 2**30, 2**40]
    y1 = [f4(x[0]), f4(x[1]), f4(x[2]), f4(x[3]), f4(x[4]), f4(x[5]), f4(x[6])]
    y2 = [f5(x[0]), f5(x[1]), f5(x[2]), f5(x[3]), f5(x[4]), f5(x[5]), f5(x[6])]

    plt.plot(x, y1, label='f4', color='blue')
    plt.plot(x, y2, label='f5', color='green')
    plt.xscale('log', base=2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('f4 vs f5 growth rates')
    plt.legend()
    plt.show()

def graph_log_n(n):
    x = []
    y = []
    for i in range(1, n+1):
        x.append(i)
        y.append(f4(i))

    plt.plot(x, y)
    plt.show()

def graph_f4_and_f5(n):
    x = []
    y1 = []
    y2 = []
    for i in range(1, n+1):
        x.append(i)
        y1.append(f4(i))
        y2.append(f5(i))

    plt.plot(x, y1, label='f4', color='blue')
    plt.plot(x, y2, label='f5', color='green')
    #plt.xscale('log', base=5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('f4 vs f5 growth rates')
    plt.legend()
    plt.show()

def graph_n_log_n(n):
    x = []
    y = []
    for i in range(1, n+1):
        x.append(i)
        y.append(n * math.log(i, 2))

    plt.plot(x, y)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #compare_f4_and_f5()
     #graph_log_n(500)
    # graph_n_log_n(500)
    graph_f4_and_f5(500000)







