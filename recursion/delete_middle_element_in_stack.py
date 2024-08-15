from collections import deque


def delete(stack_arr, mid):
    if len(stack_arr) == mid:
        stack_arr.pop()
        return stack_arr
    temp = stack_arr.pop()
    delete(stack_arr, mid)
    stack_arr.append(temp)
    return


def delete_middle_element(stack_arr):
    mid = len(stack_arr) // 2 + 1
    delete(stack_arr, mid)
    return stack_arr


if __name__ == "__main__":
    srr1 = deque([1, 2, 3, 4, 5, 6, 7])
    print(delete_middle_element(srr1))
