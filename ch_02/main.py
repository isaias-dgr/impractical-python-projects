import load_dictionary

word_list = load_dictionary.load("ch_02/file_word.txt")

pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of palindormes found={len(pali_list)} {len(word_list)}")
print(*pali_list, sep='\n')