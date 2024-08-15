from collections import deque


def insert(stack_arr, temp):
    if len(stack_arr) == 0 or stack_arr[-1] <= temp:
        stack_arr.append(temp)
        return
    val = stack_arr.pop()
    insert(stack_arr, temp)
    stack_arr.append(val)
    return


def sort_stack(stack_arr):
    if len(stack_arr) <= 1:
        return stack_arr
    temp = stack_arr.pop()
    sort_stack(stack_arr)
    insert(stack_arr, temp)
    return stack_arr


if __name__ == "__main__":
    stack1 = deque([4, 5, 1, 3, 7, 2])
    print(sort_stack(stack1))
