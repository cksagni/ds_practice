def find_min_element(nums):
    if len(nums) <= 1:
        return nums[0]
    elif nums[0] < nums[-1]:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[0] > nums[mid]:
            right = nums[mid - 1]
        else:
            left = nums[mid + 1]


def find_min_element_1(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == "__main__":
    nums1 = [2, 1]
    k = find_min_element(nums1)
    k1 = find_min_element_1(nums1)
    assert k == 1
    assert k1 == 1

    nums1 = [11, 13, 15, 17]
    k = find_min_element(nums1)
    k1 = find_min_element_1(nums1)
    assert k == 11
    assert k1 == 11

    nums1 = [3, 4, 5, 1, 2]
    k = find_min_element(nums1)
    k1 = find_min_element_1(nums1)
    assert k == 1
    assert k1 == 1
