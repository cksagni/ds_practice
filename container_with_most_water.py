from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        if curr_area > area:
            area = curr_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area


if __name__ == "__main__":
    nums1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    k = max_area(nums1)
    assert k == 49

    nums1 = [1, 1]
    k = max_area(nums1)
    assert k == 1
