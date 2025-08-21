import sys
from stats import get_character_count, get_num_words, sort_character_count

def get_book_text(filepath) -> str: 
  with open(filepath, 'r', encoding='utf-8') as file:
    return file.read()
  

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_char_count = sort_character_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_info in sorted_char_count:
        if char_info['char'].isalpha():
          print(f"{char_info['char']}: {char_info['num']}")
    


main()
