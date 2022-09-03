import load_dictionary
import time

word_list = load_dictionary.load('ch_02/file_word.txt')

def find_palingrams():
    """Find  diccitionary palingrams"""
    pali_list = []

    words = set(word_list)
    for word in words:
    # for word in word_list:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list



if __name__=="__main__":
    start = time.time()
    palingrams = find_palingrams()
    end = time.time()
    palingrams_sorted = sorted(palingrams)

    print(f"\nNumber of palingrams = {len(palingrams_sorted)}")
    print(f"Time of palingrams = {end - start}")

    for first, second in palingrams_sorted:
        print(f"{first} {second}") 
