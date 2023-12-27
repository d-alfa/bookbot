def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    characters_dict = get_characters_dict(text)
    characters_sorted_list = characters_dict_to_sorted_list(characters_dict)

    print(f"--- Begin report of {book_path} ---")
    print()
    print(f"{number_of_words} words found in the document")
    print()

    for item in characters_sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"The '{item['character']}' character was found {item['number']} times")
    print()
    print("--- End report ---")

def get_number_of_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["number"]

def characters_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for character in characters_dict:
        sorted_list.append({"character": character, "number": characters_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_characters_dict(text):
    chars = {}
    for character in text:
        lowered = character.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()