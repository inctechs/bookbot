def get_number_of_words(text:str) -> int:
    return len(text.split())

def get_number_of_characters(text:str) -> dict[str, int]:
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,!? '
    char_count = {char: 0 for char in alphabet}
    for char in alphabet:
        char_count[char] = text.count(char)
    return char_count

def get_sorted_list_of_chars(dict_chars:dict[str, int]) -> list[dict[str, int]]:
    list_chars = [{"char": char, "num": num} for char, num in dict_chars.items()]
    def sort_on(item:dict[str, int]) -> int:
        return item["num"]
    list_chars.sort(key=sort_on, reverse=True)
    return list_chars
