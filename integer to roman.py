def int_to_roman(num):
    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
        50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"
    }
    # Initialize an empty string to store the Roman numeral representation
    roman_numeral = ""
    # Iterate through the values in reverse order
    for value in sorted(roman_numerals.keys(), reverse=True):
        # Repeat subtracting the largest value possible from the input number
        while num >= value:
            roman_numeral += roman_numerals[value]
            num -= value
    return roman_numeral

# Test the function
num = 3549
print(f"Roman numeral for {num}: {int_to_roman(num)}")
