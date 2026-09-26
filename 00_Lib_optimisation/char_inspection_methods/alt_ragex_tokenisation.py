# Custom Tokenization Without Regex
# Replace non-alphanumeric separators with spaces to tokenize structured codes like serial numbers or product tags.

product_code = "SKU: 902-AX_77"

# Replace symbols/punctuation with spaces, then split
tokens = "".join(c if c.isalnum() else " " for c in product_code).split()
print(tokens)  # Output: ['SKU', '902', 'AX', '77']

# .isdigit() targets strictly 0–9.
# .isalpha() targets strictly alphabetical characters.
# .isspace() targets \n, \t, and whitespace.
# .isupper() / .islower() checks casing for casing-dependent parsing.
