# Password Rule Validation (any() with Character Checks)
# Combine comprehension checks with Python's built-in any() function to enforce security rules in a single pass.

def validate_password(password: str) -> bool:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return (
        len(password) >= 8 and has_upper and has_lower and has_digit and has_special
    )


print(validate_password("SecurePass99!"))  # True
print(validate_password("weakpass"))  # False

