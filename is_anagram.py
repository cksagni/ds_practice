

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_map = {}
    for c in s:
        if c in char_map:
            char_map[c] = char_map[c] + 1
        else:
            char_map[c] = 1
    for c in t:
        if char_map.get(c, 0) > 0:
            char_map[c] = char_map[c] - 1
        else:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("rat","tar"))
    print(is_anagram("abc", "bde"))
    print(is_anagram("bat", "batsman"))
    print(is_anagram("aab", "abc"))

