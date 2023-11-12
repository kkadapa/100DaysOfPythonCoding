from collections import Counter


def count_anagrams(word):
    # Convert the word to a tuple of its sorted characters
    return tuple(sorted(word))

def word_with_most_anagrams(word_list):
    # Dictionary to store list of anagrams
    anagram_counts = Counter()

    # Iterate through the words in the list
    for word in word_list:
        # Count anagrams based on the sorted tuple of characters
        anagram_counts[count_anagrams(word)] += 1

    # Find the word with the maximum count of anagrams
    most_anagrams = max(anagram_counts, key=anagram_counts.get)

    # Get all words with the maximum count of anagrams
    max_anagram_words = [word for word in word_list if count_anagrams(word) == most_anagrams]

    return max_anagram_words

# Example usage:
word_list = ['listen', 'silent', 'enlist', 'hello', 'world', 'dog', 'god']
result = word_with_most_anagrams(word_list)
print(f"The word(s) with the most anagrams: {result}")
