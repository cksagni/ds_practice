from typing import List

"""rotate array right by k places"""


def rotate_in_place(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    nums[n - k:n] = nums[n - 1: n - k - 1:-1]
    nums[0: n - k] = nums[n - k - 1::-1]
    nums.reverse()


def rotate_with_extra_space(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    temp = nums[n - k:n]
    start_index = n - 1
    first_rot_index = n - k - 1
    while first_rot_index >= 0:
        nums[start_index] = nums[first_rot_index]
        start_index -= 1
        first_rot_index -= 1
    while start_index >= 0:
        nums[start_index] = temp[start_index]
        start_index -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate_in_place(nums=nums1, k=3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    rotate_with_extra_space(nums1, k=4)
    assert nums1 == [1, 2, 3, 4, 5, 6, 7]

