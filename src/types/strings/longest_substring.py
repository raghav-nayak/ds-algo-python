# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150

# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# naive approach
# time complexity: O(n^2)
# space complexity: O(1)
def longest_substring_naive_approach(input_str: str) -> str:
    input_str_length = len(input_str)
    result = 0

    for i in range(input_str_length):
        visited = [False] * 256

        for j in range(i, input_str_length):
            # check whether the char is visited or not
            if visited[ord(input_str[j])] == True:
                break
            else:
                result = max(result, j - i + 1)
                visited[ord(input_str[j])] = True
    return result


# sliding window
# time complexity: O(n)
# space complexity: O(1)
def longest_substring_sliding_window(input_str: str) -> str:
    input_str_len = len(input_str)

    if input_str_len == 0:
        return 0

    if input_str_len == 1:
        return 1

    max_length = 0
    visited = [False] * 256

    start = 0
    end = 0

    while end < input_str_len:
        while visited[ord(input_str[end])] == True:
            visited[ord(input_str[start])] = False
            start += 1

        visited[ord(input_str[end])] = True

        max_length = max(max_length, end - start + 1)
        end += 1

    return max_length


# using last index of each character
# approach:
# store the last indexes of already visited characters.
def longest_substring_using_last_index(input_str: str) -> str:
    input_str_len = len(input_str)

    result = 0
    last_index = [-1] * 256

    start = 0

    for end in range(input_str_len):
        # print(f"{input_str[end]} : {start=} {end=} {last_index[ord(input_str[end])]}")
        start = max(start, last_index[ord(input_str[end])] + 1)
        result = max(result, end - start + 1)
        last_index[ord(input_str[end])] = end
        # print(f"{start=} {result=} last_index={last_index[ord(input_str[end])]}\n")

    return result


def longest_substring_best_solution_leetcode(self, s: str) -> int:
    if s == "":
        return 0
    longs = s[0]
    start = 0
    end = 1
    maxlen = 1
    while end < len(s):
        if s[end] not in longs:
            longs += s[end]
        else:
            while s[start] != s[end] and start < end:
                start += 1
            start += 1
            longs = s[start : end + 1]

        end += 1
        if maxlen < len(longs):
            maxlen = len(longs)
    return maxlen


if __name__ == "__main__":
    input_str = "GEEKSFORGEEKS"

    print(
        f"with naive approach : {longest_substring_naive_approach(input_str=input_str)}"
    )

    print(
        f"with sliding window approach : {longest_substring_sliding_window(input_str=input_str)}"
    )

    print(
        f"with sliding window approach : {longest_substring_using_last_index(input_str=input_str)}"
    )
