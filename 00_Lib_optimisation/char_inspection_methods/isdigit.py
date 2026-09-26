raw_input = "+1 (800) 555-0199"

# Retain only numeric characters
cleaned_digits = "".join(c for c in raw_input if c.isdigit())
print(cleaned_digits)  # Output: "18005550199"

# Condition: Evaluates to True strictly for characters 0 through 9.
# Behavior: Excludes +, (, ), spaces, and -.
