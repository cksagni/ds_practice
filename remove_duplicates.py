"""remove duplicates from an array sorted in non-descending order"""
from typing import List


def remove_duplicates(nums: List[int]) -> List[int]:
    move_to_index = 0
    for move_from_index in range(1, len(nums)):
        if nums[move_from_index] != nums[move_to_index]:
            move_to_index += 1
            nums[move_to_index] = nums[move_from_index]
    return nums[0:move_to_index + 1]


if __name__ == "__main__":
    nums1 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6]
    unique_elements = remove_duplicates(nums1)
    assert unique_elements == [0, 1, 2, 3, 4, 5, 6]

