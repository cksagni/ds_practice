
def find_min_window_brute(st):
    # Your code goes here
    unique = len(set(st))
    min_l = len(st)

    for i in range(len(st)):
        for j in range(i, len(st ) +1):
            temp = len(set(st[i:j]))
            if temp == unique:
                min_l = min(min_l, j- i)

    return min_l


def find_min_window_optim(st):
    unique = len(set(st))
    min_l = len(st)

    char_map = {}
    i = j = 0
    while i < len(st):

        if st[i] in char_map:
            char_map[st[i]] = char_map[st[i]] + 1
        else:
            char_map[st[i]] = 1
        i += 1
        if len(char_map) == unique:
            while char_map[st[j]] > 1:
                char_map[st[j]] = char_map[st[j]] - 1
                j += 1

        if len(char_map) == unique:
            min_l = min(min_l, i - j)

    return min_l


if __name__ == "__main__":
    s = "AABBCC"
    print(find_min_window_brute(s))
    print(find_min_window_optim(s))
    s = "aabcbcdbca"
    print(find_min_window_brute(s))
    print(find_min_window_optim(s))
