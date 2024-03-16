def roman_to_int(s):
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    # Initialize the result to store the integer value
    result = 0
    # Iterate through the input string from right to left
    for i in range(len(s) - 1, -1, -1):
        # If the current numeral is smaller than the next numeral, subtract its value
        if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
            result -= roman_numerals[s[i]]
        else:
            result += roman_numerals[s[i]]
    return result

# Test the function
roman_numeral = "MCMXCIV"
print(f"Integer value for {roman_numeral}: {roman_to_int(roman_numeral)}")
