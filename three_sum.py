from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""


def three_sum_1(nums: List[int]) -> List[List[int]]:
    triplets = set()
    n = len(nums)
    nums.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        target = 0 - nums[i]
        while left < right:
            if nums[left] + nums[right] == target:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    return [list(x) for x in triplets]


def three_sum(nums: List[int]) -> List[List[int]]:
    elm_map = {}
    triplets = set()
    for n in nums:
        if elm_map.get(n):
            elm_map[n] = elm_map[n] + 1
        else:
            elm_map[n] = 1
    for k, v in elm_map.items():
        elm_map[k] = v - 1
        for k2, v2 in elm_map.items():
            if v2 > 0:
                elm_map[k2] = v2 - 1
                target = 0 - k2 - k
                v3 = elm_map.get(target)
                if v3 and v3 > 0:
                    triplets.add(tuple(sorted([k, k2, target])))
                elm_map[k2] = v2
    return [list(x) for x in triplets]


if __name__ == "__main__":
    nums1 = [-1, 0, 1, 2, -1, -4]
    trip = three_sum(nums1)
    trip_1 = three_sum_1(nums1)
    assert trip == [[-1, 0, 1], [-1, -1, 2]]
    assert trip_1 == [[-1, 0, 1], [-1, -1, 2]]

    nums1 = [0, 1, 1]
    trip = three_sum(nums1)
    trip_1 = three_sum_1(nums1)
    assert trip == []
    assert trip_1 == []

    nums1 = [-1, 0, 1, 0]
    trip = three_sum(nums1)
    trip_1 = three_sum_1(nums1)
    assert trip == [[-1, 0, 1]]
    assert trip_1 == [[-1, 0, 1]]

    nums1 = [-2, 0, 0, 2, 2]
    trip = three_sum(nums1)
    trip_1 = three_sum_1(nums1)
    assert trip == [[-2, 0, 2]]
    assert trip_1 == [[-2, 0, 2]]

    nums1 = [3, 0, -2, -1, 1, 2]
    trip = three_sum(nums1)
    trip_1 = three_sum_1(nums1)
    assert trip == [[-2, -1, 3], [-1, 0, 1], [-2, 0, 2]]
    assert trip_1 == [[-2, -1, 3], [-1, 0, 1], [-2, 0, 2]]
