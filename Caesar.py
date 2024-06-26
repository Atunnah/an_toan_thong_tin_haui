def create_vietnamese_alphabet():
    # Base characters without diacritics
    base_chars = "AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYZaăâbcdđeêghiklmnôoơpqrstuưvxy"
    
    # Diacritical marks
    diacritics = ["", "̀", "́", "̉", "̃", "̣"]  # including no diacritic, grave, acute, hook, tilde, and dot below

    # Initialize an empty dictionary
    vietnamese_alphabet = {}

    # Generate all possible combinations of base characters and diacritics
    for char in base_chars:
        for diacritic in diacritics:
            combined_char = char + diacritic
            vietnamese_alphabet[combined_char] = combined_char
    
    return vietnamese_alphabet

# Calling the function and printing the result
vietnamese_alphabet = create_vietnamese_alphabet()
print(vietnamese_alphabet)
