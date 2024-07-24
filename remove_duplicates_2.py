from typing import List


def remove_duplicates(nums: List[int]) -> int:
    count = 1
    index = 1
    prev_elm = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != prev_elm:
            nums[index] = nums[i]
            index += 1
            count = 1
            prev_elm = nums[i]
        elif count < 2:
            nums[index] = nums[i]
            index += 1
            count += 1
    return index


if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3, 4, 4, 4]
    k = remove_duplicates(nums1)
    assert [1, 1, 2, 2, 3, 4, 4] == nums1[0:k]

    nums2 = [1, 1]
    k = remove_duplicates(nums2)
    assert [1, 1] == nums2[0:k]

    nums3 = [1, 2]
    k = remove_duplicates(nums3)
    assert [1, 2] == nums3[0:k]