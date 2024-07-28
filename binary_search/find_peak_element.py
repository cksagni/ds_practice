from typing import List


# code to find peak element in linear time i.e. O(n)
def find_peak_element(nums: List[int]) -> int:
    i = 1
    if len(nums) == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1
    while i < len(nums) - 1:
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
        i += 1


# code to find peak element in logarithmic time i.e. O(log n)
def find_peak_element_1(nums: List[int]) -> int:
    i = 1
    if len(nums) == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid + 1] > nums[mid]:
            left = mid
        else:
            right = mid


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    k = find_peak_element(nums1)
    k1 = find_peak_element_1(nums1)
    assert k == 2
    assert k1 == 2

    nums1 = [1, 2, 1, 3, 5, 6, 4]
    k = find_peak_element(nums1)
    k1 = find_peak_element_1(nums1)
    assert k in [1, 5]
    assert k1 in [1, 5]
