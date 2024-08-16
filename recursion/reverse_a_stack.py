from collections import deque


def reverse_stack_extra_space(stack_arr, rev_stack=deque()):
    if len(stack_arr) <= 1:
        rev_stack.append(stack_arr.pop())
        return
    rev_stack.append(stack_arr.pop())
    reverse_stack_extra_space(stack_arr)
    return rev_stack


def insert(stack_arr, temp):
    if len(stack_arr) == 0:
        stack_arr.append(temp)
        return
    val = stack_arr.pop()
    insert(stack_arr, temp)
    stack_arr.append(val)
    return


def reverse_stack_constant_space(stack_arr):
    if len(stack_arr) <= 1:
        return stack_arr
    temp = stack_arr.pop()
    reverse_stack_constant_space(stack_arr)
    insert(stack_arr, temp)
    return stack_arr


if __name__ == "__main__":
    srr1 = deque([1, 2, 3, 4, 5, 6, 7])
    print(reverse_stack_constant_space(srr1))
