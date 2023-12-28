
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







