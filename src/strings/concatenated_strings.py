# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150

# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.


# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].


# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.


from typing import List

# note: partial solution
def find_sub_string(s: str, words: List[str]) -> List[int]:
    result = list()
    if not words or not s:
        return result

    s_len = len(s)
    words_list_len = len(words)
    word_len = len(words[0])
    # target_len = words_list_len * word_len
    print(f"{word_len=} {words_list_len=}")

    start = 0
    end = 0

    while end < s_len:
        print(f"\n\n{start=} {end=}")
        count = 0
        word_check = s[end : end + word_len]
        inner_end = end
        while word_check in words:
            print(f"1 - {word_check=} {count=} {words_list_len=}")
            count += 1
            inner_end += word_len
            word_check = s[inner_end : inner_end + word_len]

            print(f"2 - {word_check=} {count=} {words_list_len=}")
            if count == words_list_len:
                result.append(start)
                continue
        start += word_len
        end += word_len

    return result


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    # print(f"{find_sub_string(s=s, words=words)}")

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    print(f"{find_sub_string(s=s, words=words)}")
