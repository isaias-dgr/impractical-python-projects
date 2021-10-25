from pprint import PrettyPrinter
import string

def get_poor_mans_bar_char(paragraph):
    bars = get_bars()
    letters = paragraph.lower().replace(" ","")
    for l in letters:
        if l.isalpha():
            bars[l].append(l)
    return bars

def get_bars():
    return {letter: [] for letter in string.ascii_lowercase}

if __name__ == "__main__":
    p = PrettyPrinter(2)
    paragraph = """Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much."""
    print(paragraph)
    p.pprint(get_poor_mans_bar_char(paragraph))