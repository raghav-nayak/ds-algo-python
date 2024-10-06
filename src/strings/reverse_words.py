# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

import re

def reverse_words_using_inbuilt_func(s: str) -> str:
    # return " ".join(s.split(" ")[-1::-1])
    return re.sub(r"\s+", " ", " ".join(s.split(" ")[-1::-1])).strip()

    # def reverse_word(s: str) -> str:
    #     end = len(s) - 1
    #     reversed_str = str()

    #     while end >= 0:
    #         if s[end] == " ":
    #             end -= 1
    #         else:


def reverse_words_best_soln_leetcode(s: str) -> str:
    words = s.split()

    l, r = 0, len(words) - 1
    while l < r:
        temp = words[l]
        words[l] = words[r]
        words[r] = temp

        l += 1
        r -= 1

    return " ".join(words)


if __name__ == "__main__":
    s = "the sky is blue"
    print(f"{reverse_words_using_inbuilt_func(s)}")
    print(f"{reverse_words_best_soln_leetcode(s)}")

    s = "  hello world  "
    print(f"{reverse_words_using_inbuilt_func(s)}")
    print(f"{reverse_words_best_soln_leetcode(s)}")

    s = "a good   example"
    print(f"{reverse_words_using_inbuilt_func(s)}")
    print(f"{reverse_words_best_soln_leetcode(s)}")
