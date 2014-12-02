# Simple Python primes finder
import numpy as np


def primes(kmax):
    p = np.empty(1000)
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
        n = n + 1
    return p[0:k]
