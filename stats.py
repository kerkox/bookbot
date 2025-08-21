def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_character_count(text: str) -> dict[str, int]:
    char_count = {}
    for char in text:
        char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

def sort_character_count(char_count: dict[str, int]):
    result = []
    for char, count in char_count.items():
        tempDict = { "char": char, "num": count }
        result.append(tempDict)
    result.sort(key=lambda x: x["num"], reverse=True)
    return result