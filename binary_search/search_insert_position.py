from typing import List


def search_insert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    return left


if __name__ == "__main__":
    nums1 = [1, 3, 5, 6]
    k = search_insert(nums1, 5)
    assert k == 2

    nums1 = [1, 3, 5, 6]
    k = search_insert(nums1, 2)
    assert k == 1

    nums1 = [1, 3, 5, 6]
    k = search_insert(nums1, 7)
    assert k == 4

    nums1 = [1, 3, 5, 6]
    k = search_insert(nums1, 0)
    assert k == 0

    nums1 = [1]
    k = search_insert(nums1, 1)
    assert k == 0

