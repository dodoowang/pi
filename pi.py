from decimal import Decimal, getcontext
from time import time
from math import factorial


def leibniz():
    def deltan(n):
        four_n = 4 * Decimal(n)
        return Decimal(8) / (four_n + Decimal(1)) / (four_n + Decimal(3))

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield result
        n += 1


def euler():
    def deltan(n):
        a = Decimal(pow(2, n) * pow(factorial(n), 2))
        b = Decimal(factorial(2 * n + 1))
        return Decimal(2) * a / b

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield result
        n += 1


def machin():
    def deltan(n):
        two_n_plus_one = Decimal(2) * Decimal(n) + Decimal(1)
        a = Decimal(4) * pow(Decimal(5), Decimal(-1 * two_n_plus_one))
        b = pow(Decimal(239), Decimal(-1 * two_n_plus_one))
        return Decimal(4) * pow(-1, n) / two_n_plus_one * (a - b)

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield result
        n += 1


def plouffe():
    def deltan(n):
        a = Decimal(2) / Decimal(4 * n + 1)
        b = Decimal(2) / Decimal(4 * n + 2)
        c = Decimal(1) / Decimal(4 * n + 3)
        return pow(-1, n) / pow(Decimal(4), Decimal(n)) * (a + b + c)

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield result
        n += 1


def gauss():
    def deltan(n):
        x = Decimal(2 * n + 1)
        a = Decimal(12) * pow(Decimal(38), -x)
        b = Decimal(20) * pow(Decimal(57), -x)
        c = Decimal(7) * pow(Decimal(239), -x)
        d = Decimal(24) * pow(Decimal(268), -x)

        return Decimal(4) * pow(-1, n) / x * (a + b + c + d)

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield result
        n += 1


def ramanujan():
    def deltan(n):
        a = factorial(4 * n) * (1103 + 26390 * n)
        b = pow(factorial(n), Decimal(4))
        c = 396 ** (4 * n)
        return Decimal(a) / Decimal(b) / Decimal(c)

    n = 0
    result = 0
    while True:
        result += deltan(n)
        yield Decimal(9801) / Decimal(8).sqrt() * (Decimal(1) / result)
        n += 1


def salamin():
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    u = Decimal(0)
    v = Decimal(1)
    while True:
        a, b, u, v = \
            (a + b) / Decimal(2), \
            Decimal(a * b).sqrt(), \
            (u + v) / Decimal(2), \
            (u * b + v * a) / Decimal(2) / Decimal(a * b).sqrt()
        yield Decimal(8).sqrt() * pow(a, Decimal(3)) / u


def borwein1984():
    a = Decimal(2).sqrt()
    b = Decimal(0)
    p = Decimal(2) + Decimal(2).sqrt()
    while True:
        a, b = a.sqrt() / Decimal(2) + Decimal(1/2) / a.sqrt(), \
                a.sqrt() * (Decimal(1) + b) / (a + b)
        p = p * b * (Decimal(1) + a) / (Decimal(1) + b)
        yield p


def borwein1987():
    y = Decimal(2).sqrt()
    y = (Decimal(1) + y) / Decimal(2) / y.sqrt()
    z = pow(Decimal(2), Decimal(1/4))
    f = Decimal(2) + Decimal(2).sqrt()
    while True:
        f = f * (Decimal(1) + y) / (Decimal(1) + z)
        yield f
        y, z = (Decimal(1) + y) / Decimal(2) / y.sqrt(), \
            (Decimal(1) + y * z) / (Decimal(1) + z) / y.sqrt()


def pi_calc(f, prec=100, verb=True):
    '''
    calculate pi value to given precision level with different algorthims

    f: the algorithm to be used. now following algorithms are implemented:
        - leibniz: lowest efficient
        - euler
        - plouffe
        - machin
        - gauss: very fast
        - ramanujan: like magic
        - salamin: extreamly fast
        - borwein1984: similar to salamin
        - veorwein1987: similar to salamin
    prec: the precision level required. default setting is 100 digits
    verb: if verbose is True, then the process will be printed. default is True

    examples:
        python pi.py gauss 150
        python pi.py salamin 1000 --verb 0


    remark: please refer to http://www.pi314.net/eng/accueilformules.php for
    all these algorithms
    '''
    f = globals()[f]
    getcontext().prec = prec
    tic = time()
    check_point = 1
    pi_prev = -1
    for n, pi in enumerate(f()):
        if verb and (n == 0 or n % check_point == 0):
            print("n = {:7d}: {}".format(n, pi))
            check_point *= 2
        if pi_prev == pi or n == 1e6:
            print("n = {:7d}: {}".format(n, pi))
            break
        pi_prev = pi
    print("{} in {} seconds, {} rounds".format(f.__name__, time() - tic, n))
    if n >= 1e6:
        print("{} cannot converge in {} rounds".format(f.__name__, n))


if __name__ == "__main__":
    import fire
    fire.Fire(pi_calc)
