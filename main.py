def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words found in the document")
    print()

    counted_dict = character_count(text)
    counted_list = char_count_as_list(counted_dict)
    sorted_printer(counted_list)

    print("--- End report ---")

#ingest and print book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words
def word_count(file):
    words = file.split()
    return len(words)

#count characters by character
def character_count(file):
    counts = {}
    lowered_file = file.lower()
    for character in lowered_file:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1
    return counts

def char_count_as_list(count_dict):
    count_list = []
    for key, value in count_dict.items():
        if key.isalpha():
            count_list.append({"name": key, "count": value})
    
    count_list.sort(reverse=True, key=sort_on)
    return count_list
    
def sort_on(dict):
    return dict["count"]

def sorted_printer(sorted_list):
    for item in sorted_list:
        print(f"The '{item["name"]}' character was found {item["count"]} times")


main()
