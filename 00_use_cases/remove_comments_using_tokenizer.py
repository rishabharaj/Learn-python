import tokenize

with open("input.py", "r", encoding="utf-8") as f:
    tokens = tokenize.generate_tokens(f.readline)

    filtered = []

    for token in tokens:
        if token.type != tokenize.COMMENT:
            filtered.append(token)

with open("output.py", "w", encoding="utf-8") as f:
    f.write(tokenize.untokenize(filtered))
