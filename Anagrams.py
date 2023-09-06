def find_anagrams(word, word_list):
    sorted_word = sorted(word)
    anagrams = []

    for candidate in word_list:

        sorted_candidate = sorted(candidate)

        if sorted_candidate == sorted_word:
            anagrams.append(candidate)

    return anagrams

#input word and list of words to check anagram
input_word = "listen"
word_list = ["enlist", "silent", "hello", "world", "teen", "dad", "dislike"]

result = find_anagrams(input_word, word_list)

if result:
    print(f"Anagrams of '{input_word}': {result}")
else:
    print(f"No anagrams of '{input_word}' found in the list.")
