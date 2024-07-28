from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    left = 0
    right = m = len(matrix) - 1
    n = len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            if matrix[mid][n] >= target:
                left = mid
                break
            else:
                left = mid + 1
        else:
            right = mid - 1
    i = min(left, m)
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if matrix[i][mid] == target:
            return True
        elif matrix[i][mid] < target:
             left = mid + 1
        else:
             right = mid - 1
    return False


def search_matrix_1(matrix, target):
    left = 0
    m = len(matrix)
    n = len(matrix[0])
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        mid_row, mid_col = divmod(mid, n)
        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    nums1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    k = search_matrix(nums1, 13)
    assert k is False
    k = search_matrix_1(nums1, 13)
    assert k is False

    nums1 = [[1]]
    k = search_matrix(nums1, 2)
    assert k is False
    k = search_matrix_1(nums1, 2)
    assert k is False

    nums1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    k = search_matrix(nums1, 30)
    assert k is True
    k = search_matrix_1(nums1, 30)
    assert k is True






