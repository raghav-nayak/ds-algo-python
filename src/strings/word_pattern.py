# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false


# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


def word_pattern(pattern: str, s: str) -> bool:
    pattern_word_map = dict()
    word_pattern_map = dict()

    s_list = s.split(" ")
    s_list_len = len(s_list)
    if s_list_len != len(pattern):
        return False

    for idx in range(s_list_len):
        if val := pattern_word_map.get(pattern[idx]):
            if val == s_list[idx]:
                continue
            else:
                return False
        else:
            pattern_word_map.update({pattern[idx]: s_list[idx]})

        if val := word_pattern_map.get(s_list[idx]):
            if val == pattern[idx]:
                continue
            else:
                return False
        else:
            word_pattern_map.update({s_list[idx]: pattern[idx]})

    return True


def word_pattern_best_soln_leetcode(pattern: str, s: str) -> bool:
    # Split the input string s into words
    words = s.split()

    # If the length of the pattern doesn't match the number of words, return False
    if len(pattern) != len(words):
        return False

    # Dictionaries to map pattern to words and vice versa
    pattern_to_word = {}
    word_to_pattern = {}

    # Iterate through the pattern and words simultaneously
    for p, word in zip(pattern, words):
        # Check if the pattern has been encountered before
        if p in pattern_to_word:
            # If it has, check if it maps to the current word
            if pattern_to_word[p] != word:
                return False
        else:
            # If the pattern hasn't been encountered, add it to the dictionary
            pattern_to_word[p] = word

        # Check if the word has been encountered before
        if word in word_to_pattern:
            # If it has, check if it maps to the current pattern character
            if word_to_pattern[word] != p:
                return False
        else:
            # If the word hasn't been encountered, add it to the dictionary
            word_to_pattern[word] = p

    # If all checks pass, return True
    return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    print(word_pattern(pattern, s))
    print(word_pattern_best_soln_leetcode(pattern, s))

    pattern = "abba"
    s = "dog cat cat fish"
    print(word_pattern(pattern, s))
    print(word_pattern_best_soln_leetcode(pattern, s))

    pattern = "aaaa"
    s = "dog cat cat dog"
    print(word_pattern(pattern, s))
    print(word_pattern_best_soln_leetcode(pattern, s))

    pattern = "abba"
    s = "dog dog dog dog"
    print(word_pattern(pattern, s))
    print(word_pattern_best_soln_leetcode(pattern, s))
