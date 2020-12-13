from common import get_input
from functools import reduce


def chinese_remainder(n, a):
    # O(nlogn) time and O(n) space
    # From https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
    

if __name__ == "__main__":
    _, buses = get_input()
    offsets = [int(b) - i for i, b in enumerate(buses) if b != "x"]
    buses = [int(b) for b in buses if b != "x"]
    print(chinese_remainder(buses, offsets))
