
def subsequence(ip, op="", all_op=set()):
    if len(ip) == 0:
        all_op.add(op)
        return
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    subsequence(ip, op1)
    subsequence(ip, op2)
    return all_op


if __name__ == "__main__":
    s = "abcd"
    print(subsequence(s))
