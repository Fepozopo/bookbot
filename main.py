from stats import count_words, count_characters

# Open book and read
def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document.")
    print("", end = "\n")
    count_characters(text)
    print("", end = "\n")
    print("--- End report ---")


main()