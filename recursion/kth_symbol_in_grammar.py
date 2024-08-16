import math


def kth_symbol(n, k):
    if n == 1:
        return 0
    mid = 2 ** (n - 2)
    if k > mid:
        return 1 ^ kth_symbol(n-1, k-mid)
    return kth_symbol(n-1, k)


def kth_symbol_iterative(n, k):
    k -= 1
    s = 0
    for x in range(n, 1, -1):
        mid = 2 ** (x - 1) // 2
        if k >= mid:
            s ^= 1
            k -= mid
    return s


if __name__ == "__main__":
    i = 5; j = 10;
    print(kth_symbol(i, j))

    print(kth_symbol_iterative(i, j))