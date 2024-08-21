

def powerset(ip, op=[], all_items=set()):
    if len(ip) == 0:
        all_items.add(tuple(op))
        return
    op1 = op
    op2 = op1 + [ip[0]]
    ip = ip[1:]
    powerset(ip, op1)
    powerset(ip, op2)
    return all_items


def powerset_iterative(nums):
    complete_subset = [[]]
    for num in nums:
        temp_subsets = []
        for curr in complete_subset:
            temp = curr.copy()
            temp.append(num)
            temp_subsets.append(temp)
        complete_subset += temp_subsets
    return complete_subset


if __name__ == "__main__":
    s = [1, 2, 3, 4]
    print(powerset(sorted(s)))
    print(powerset_iterative(s))
