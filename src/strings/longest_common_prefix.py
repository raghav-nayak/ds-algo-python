# https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    strs_len = len(strs)
    prefix = str()
    if strs_len < 1:
        return

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, strs_len):
            if i >= len(strs[j]) or char != strs[j][i]:
                return prefix
        prefix += char
    return prefix


def longest_common_prefix_best_soln_from_leetcode(strs: List[str]) -> str:
    strs = sorted(strs)
    result = str()
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result += first[i]
    return result


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs))
    print(longest_common_prefix_best_soln_from_leetcode(strs))

    strs = ["dog", "racecar", "car"]
    print(longest_common_prefix(strs))
    print(longest_common_prefix_best_soln_from_leetcode(strs))
