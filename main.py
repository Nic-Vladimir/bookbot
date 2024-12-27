import sys

def main() -> int:
    """Program entry point"""
    book_path = "books/frankenstein.txt"
    file_contents = get_file_contents(book_path)
    word_count = get_word_count(file_contents)
    char_dict = count_chars(file_contents)
    char_sorted_list = sort_dict(char_dict)

    print(f"--- Begin report of book: Frankenstein ---")
    print(f"{word_count} words found in the document.")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times.")

    print("--- End report ---")
    return 0

def get_file_contents(file_path) -> str:
    """Reads the contents of a file"""
    with open(file_path) as f:
        return f.read()

def get_word_count(file_contents) -> int:
    """Returns the number of words in the file"""
    words = file_contents.split()
    return len(words)

def count_chars(file_contents) -> int:
    """Returns the number of characters in the file"""
    chars = {}
    text = file_contents.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(item) -> int:
    """Returns the value of the item in a dictionary"""
    return item["num"]

def sort_dict(chars_dict) -> list:
    """Sorts a dictionary by value"""
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

if __name__ == "__main__":
    sys.exit(main())
