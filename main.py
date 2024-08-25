# Open book and read
def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document.")
    print("", end = "\n")
    print(count_characters(text))
    print("--- End report of books/frankenstein.txt ---")
          

# Count words of text
def count_words(text):
    w = text.split()
    words = len(w)

    return words


# Count characters of text
def count_characters(text):
    lower_text = text.lower()
    characters = {}
    for i in lower_text:
        if i in characters and i.isalpha():
            characters[i] += 1
        elif i.isalpha():
            characters[i] = 1

    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)

    for k in sorted_characters:
        print(f"The '{k[0]}' character was found {k[1]} times.")



main()