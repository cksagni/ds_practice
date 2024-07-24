from typing import List


def remove_element(nums: List[int], val: int) -> int:
    last_index = len(nums) - 1
    index = 0
    while last_index >= 0 and nums[last_index] == val:
        last_index -= 1
    while last_index >= 0 and index < last_index:
        if nums[index] == val:
            nums[index] = nums[last_index]
            nums[last_index] = val
            last_index -= 1
        while nums[last_index] == val:
            last_index -= 1
        index += 1
    return last_index + 1


def remove_element_1(nums: List[int], val: int) -> int:
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    k = remove_element(nums1, 3)
    assert [2, 2] == nums1[0:k]

    nums2 = [1]
    k = remove_element(nums2, 1)
    assert [] == nums2[0:k]

    nums1 = [3, 2, 2, 3]
    k = remove_element_1(nums1, 3)
    assert [2, 2] == nums1[0:k]

    nums2 = [1]
    k = remove_element_1(nums2, 1)
    assert [] == nums2[0:k]
