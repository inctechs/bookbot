from stats import get_number_of_words, get_number_of_characters, get_sorted_list_of_chars
import sys

def get_book_text(path:str) -> str:
    with open(path) as f:
        return f.read()

def print_report(total_word_count: int, list_chars:list[dict[str, int]], book_path: str) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("------- Character Count ---------")
    for item in list_chars:
        char = item["char"]
        num = item["num"]
        if char == " ":
            char = "space"
        print(f"{char}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    num_chars = get_number_of_characters(text)
    list_chars = get_sorted_list_of_chars(num_chars)
    print_report(num_words, list_chars, book_path)

if __name__ == "__main__":
    main()
