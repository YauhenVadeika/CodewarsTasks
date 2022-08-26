# my task solution
def duplicate_count(text):
    text = text.lower()
    chars = {char: text.count(char) for char in text}
    return len([char for char in chars if chars[char] >= 2])


print(duplicate_count("indivisibility"))


# dewars task best solution
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


# dewars task best solution
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)
