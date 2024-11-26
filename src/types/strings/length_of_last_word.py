# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


def length_of_last_word_using_inbuilt_function(s: str) -> int:
    return len(list(s.strip().split(" "))[-1])


def length_of_last_word_using_sliding_window(s: str) -> int:
    last_word_len = str()
    if not s:
        return 0

    start = 0
    s_len = len(s)
    end = 0

    while end < s_len:
        # print(f"{start=} {s[start]=} {end=} {s[end]=} {last_word_len=}")
        if s[start] == " " and s[end] == " ":
            pass
        elif s[start] == " " and s[end] != " ":
            start = end
        elif s[start] != " " and s[end] != " ":
            pass
        elif s[start] != " " and s[end] == " ":
            last_word_len = s[start:end]
            # print(f"===> {last_word_len=}")
            start = end
        end += 1

    # print(f"{start=} {end=} {last_word_len=}")
    if s[start] != " " and s[end - 1] != " ":
        last_word_len = s[start:end]
        # print(f"===> {last_word_len=}")

    return len(last_word_len)


def length_of_last_word_best_soln_leetcode(s: str) -> int:
    i = len(s) - 1
    while s[i] == " ":
        i -= 1
    x = i
    while x >= 0 and s[x] != " ":
        x -= 1
    return i - x


if __name__ == "__main__":
    s = "Hello World"
    print(f"{s=} -> {length_of_last_word_using_sliding_window(s)}")
    print(f"{s=} -> {length_of_last_word_using_inbuilt_function(s)}")
    print(f"{s=} -> {length_of_last_word_best_soln_leetcode(s)}")

    s = "   fly me   to   the moon  "
    print(f"{s=} -> {length_of_last_word_using_sliding_window(s)}")
    print(f"{s=} -> {length_of_last_word_using_inbuilt_function(s)}")
    print(f"{s=} -> {length_of_last_word_best_soln_leetcode(s)}")

    s = "luffy is still joyboy"
    print(f"{s=} -> {length_of_last_word_using_sliding_window(s)}")
    print(f"{s=} -> {length_of_last_word_using_inbuilt_function(s)}")
    print(f"{s=} -> {length_of_last_word_best_soln_leetcode(s)}")

    s = " a"
    print(f"{s=} -> {length_of_last_word_using_sliding_window(s)}")
    print(f"{s=} -> {length_of_last_word_using_inbuilt_function(s)}")
    print(f"{s=} -> {length_of_last_word_best_soln_leetcode(s)}")
