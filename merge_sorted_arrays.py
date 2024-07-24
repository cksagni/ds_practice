"""Merge two arrays sorted in non-decreasing order"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    move_to_ptr = m + n - 1
    ptr1 = m - 1
    ptr2 = n - 1

    while ptr2 >= 0:
        if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
            nums1[move_to_ptr] = nums1[ptr1]
            ptr1 -= 1
        else:
            nums1[move_to_ptr] = nums2[ptr2]
            ptr2 -= 1
        move_to_ptr -= 1
        print(ptr1, ptr2, move_to_ptr)


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 0, 0, 0]
    arr2 = [2, 4, 6]
    merge(arr1, 4, arr2, 3)
    assert arr1 == [1, 2, 3, 4, 5, 6, 7]

    arr1 = [1]
    arr2 = []
    merge(arr1, 1, arr2, 0)
    assert arr1 == [1]

    arr1 = [2, 0]
    arr2 = [1]
    merge(arr1, 1, arr2, 1)
    print(arr1)
    assert arr1 == [1, 2]





