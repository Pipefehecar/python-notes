def get_text_info(text: str) -> dict:
    return {
        "text": text,
        "length": len(text),
        "words": (words := len(text.split())),
        "characters": (letters := len(text.replace(" ", ""))),
        "vowels": (vowels := sum(1 for char in text if char.lower() in "aeiou")),
        "average_word_length": round(letters / words, 2),
        "average_vowels_per_word": round(vowels / words, 2),
    }


def walrus_chat() -> None:
    while (text := input("Enter a text: ")) != "exit":
        print(text)
    else:
        print("Goodbye!")

def dict_formatter(dictionary: dict) -> None:
    for key, value in dictionary.items():
        print(key, value, sep=": ")

if __name__ == "__main__":
    text_info = get_text_info("Mañana sera bonito!")
    dict_formatter(text_info)

    walrus_chat()