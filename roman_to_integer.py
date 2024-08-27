

def roman_to_int(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    prev_val = 0
    for c in s[::-1]:
        val = roman[c]
        if val >= prev_val:
            total += val
        else:
            total -= val
        prev_val = val
    return total



if __name__ == "__main__":
    print(roman_to_int("III"))
    print(roman_to_int("LVIII"))
    print(roman_to_int("MCMXCIV"))