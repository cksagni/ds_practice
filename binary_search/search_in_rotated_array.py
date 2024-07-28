from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # otherwise right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    nums1 = [3, 4, 5, 6, 0, 1, 2]
    k = search(nums1, 6)
    assert k == 3

    nums1 = [3, 4, 5, 6, 0, 1, 2]
    k = search(nums1, 0)
    assert k == 4

    nums1 = [4, 5, 6, 7, 0, 1, 2]
    k = search(nums1, 3)
    assert k == -1

    nums1 = [1]
    k = search(nums1, 0)
    assert k == -1
