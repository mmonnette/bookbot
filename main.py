def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(word_count(text))

#ingest and print book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count words
def word_count(file):
    words = file.split()
    return len(words)

main()
