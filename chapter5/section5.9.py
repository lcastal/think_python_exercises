
def do_n(fun, n):
    """
    Function that repeat n time fun

    :param fun: object function
    :param n: number of repetition
    """
    if n == 0:
        return
    else:
        fun()
        do_n(fun, n-1)



