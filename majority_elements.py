from typing import List


def majority_element(nums: List[int]) -> int:
    count_map = {}
    majority = len(nums )//2
    for n in nums:
        if count_map.get(n):
            count_map[n] = count_map[n] + 1
        else:
            count_map[n] = 1
    for k, v in count_map.items():
        if v > majority:
            return k


# moore voting algo
def majority_element_2(nums: List[int]) -> int:
    candidate = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = nums[i]
            count = 1
    return candidate


if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 1, 1, 1, 1, 1]
    elm1 = majority_element(nums1)
    elm2 = majority_element_2(nums1)
    assert elm1 == 1
    assert elm2 == 1

    nums1 = [1, 1, 3, 2, 1]
    elm1 = majority_element(nums1)
    elm2 = majority_element_2(nums1)
    assert elm1 == 1
    assert elm2 == 1

    nums1 = [1]
    elm1 = majority_element(nums1)
    elm2 = majority_element_2(nums1)
    assert elm1 == 1
    assert elm2 == 1

