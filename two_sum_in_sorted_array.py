from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return [0]


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    k = two_sum(nums1, 9)
    assert k == [1, 2]

    nums1 = [2, 3, 4]
    k = two_sum(nums1, 6)
    assert k == [1, 3]

    nums1 = [-1, 0]
    k = two_sum(nums1, -1)
    assert k == [1, 2]
