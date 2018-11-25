from time import time


def mc0(nr):
    n_in_circle = 0
    for i in range(nr):
        x = i / nr + .5 / nr
        for j in range(nr):
            y = j / nr + .5 / nr
            if x * x + y * y <= 1.:
                n_in_circle += 1
    return 4. * n_in_circle / nr / nr


def mc1(nr):
    nr2 = nr * nr
    n_in_circle = 0
    for i in range(nr):
        x = i + .5
        for j in range(nr):
            y = j + .5
            if x * x + y * y <= nr2:
                n_in_circle += 1
    return 4. * n_in_circle / nr2


def mc2(nr):
    nr2 = nr * nr
    n_in_circle = 0
    for i in range(nr):
        x = i + .5
        if 2 * x * x <= nr2:
            n_in_circle += 1
        for j in range(i):
            y = j + .5
            if x * x + y * y <= nr2:
                n_in_circle += 2
    return 4. * n_in_circle / nr2


def mc3(nr):
    nr2 = nr * nr
    nr_lb = 0.7 * nr
    n_in_circle = 0
    for i in range(nr):
        x = i + .5
        if 2 * x * x <= nr2:
            n_in_circle += 1
        for j in range(i):
            if x < nr_lb:
                n_in_circle += 2
                continue
            y = j + .5
            if x * x + y * y <= nr2:
                n_in_circle += 2
    return 4. * n_in_circle / nr2


def pseudo_mc(f, nr=1000):
    '''
    estimate pi with pseudo monte carlo simulation.

    f: the simulation method to be used.
        mc1: original method. space = 0~nr & 0~nr
        mc2: reduce the space into triangle. space = 0~nr & 0~x
        mc3: further reduce the space. space = 0~nr/sqrt(2) & 0~x

    nr: size of the space

    examples:
        python pseudo_mc_pi.py mc1
        python pseudo_mc_pi.py mc3 10000
    '''
    f = globals()[f]
    tic = time()
    pi = f(nr)
    toc = time()
    print("pi ~ {}. done in {} seconds.".format(pi, toc-tic))


if __name__ == "__main__":
    # import fire
    # fire.Fire(pseudo_mc)
    pseudo_mc("mc1", 10000)
    pseudo_mc("mc2", 10000)
    pseudo_mc("mc3", 10000)
