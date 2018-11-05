from time import time

nr = 100000
nr2 = nr ** 2


n_in_circle = 0
tic = time()
for i in range(nr):
    for j in range(nr):
        if i * i + j * j < nr2:
            n_in_circle += 1
toc = time()
print("pi ~ {}, in {} seconds".format(4. * n_in_circle / nr2, toc - tic))

n_in_circle = 0
tic = time()
for i in range(nr):
    for j in range(i):
        if i * i + j * j < nr2:
            n_in_circle += 1
toc = time()
print("pi ~ {}, in {} seconds".format(8. * n_in_circle / nr2, toc - tic))


n_out_circle = 0
tic = time()
for i in range(int(1.414 * nr / 2), nr):
    for j in range(i):
        if i * i + j * j >= nr2:
            n_out_circle += 1
n_in_circle = nr2 / 2 - n_out_circle
toc = time()
print("pi ~ {}, in {} seconds".format(8. * n_in_circle / nr2, toc - tic))
