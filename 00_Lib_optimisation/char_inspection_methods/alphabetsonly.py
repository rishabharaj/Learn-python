# Isolate Words for Natural Language Processing (.isalpha())
# Remove digits, underscores, and symbols when preparing raw text for word counts, sentiment analysis, or anagram checks.

raw_comment = "Order #4829 arrived super-fast! Loved it :)"

# Keep letters and spaces, drop numbers and punctuation
cleaned_text = "".join(c.lower() for c in raw_comment if c.isalpha() or c.isspace())
print(cleaned_text.split())
# Output: ['order', 'arrived', 'superfast', 'loved', 'it']

# Condition: Evaluates to True for letters a–z and A–Z.
# Behavior: Drops #4829, -, !, and :), leaving pure text tokens.
