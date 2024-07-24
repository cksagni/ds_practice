from typing import List


def max_profit(prices: List[int]) -> int:
    cheapest = prices[0]
    profit = 0
    for p in prices:
        if p < cheapest:
            cheapest = p
        elif p - cheapest > profit:
            profit = p - cheapest
    return profit


if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3, 4, 4, 4]
    pr = max_profit(nums1)
    assert 3 == pr

    nums1 = [7, 1, 5, 3, 6, 4]
    pr = max_profit(nums1)
    assert 5 == pr

    nums1 = [7, 6, 4, 3, 1]
    pr = max_profit(nums1)
    assert 0 == pr
