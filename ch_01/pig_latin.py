def traslate_to_pig_latin(paragraph):
    words = paragraph.split(" ")
    words_pig_latin = []
    for word in words:
        words_pig_latin.append(traslate_word_to_pig_latin(word))
    return " ".join(words_pig_latin)

def traslate_word_to_pig_latin(word):
    if word[0].lower() in "aeiou":
        prefix, sufix = fix_puntation(word)
        return  f"{prefix}way{sufix}"
    else:
        prefix = word[1:] .capitalize() if word[0].isupper() else word[1:]
        prefix, sufix = fix_puntation(prefix)
        return f"{prefix}{word[0].lower()}ay{sufix}"

def fix_puntation(word):
    sufix = word[-1] if not word[-1].isalnum() else ""
    prefix = word[:-1] if sufix else word
    return  prefix, sufix


if __name__ == "__main__":
    paragraph = """Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."""
    print(paragraph)
    print(traslate_to_pig_latin(paragraph))