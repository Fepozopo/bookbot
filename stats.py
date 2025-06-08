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
        print(f"{k[0]}: {k[1]}")
