

def solve(ip, op, all_perm=[]):
    if len(ip) == 0:
        all_perm.append(op)
        return

    op1 = op + ip[0]
    op2 = op + " " + ip[0]
    ip = ip[1:]
    solve(ip, op1)
    solve(ip, op2)
    return all_perm


def all_permutation(ip):
    op = ip[0]
    ip = ip[1:]
    return solve(ip, op)


if __name__ == "__main__":
    s = "abc"
    print(all_permutation(s))
