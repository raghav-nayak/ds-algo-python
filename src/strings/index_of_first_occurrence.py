# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


def str_str_inbuilt(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def str_str(haystack: str, needle: str) -> int:
    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_haystack < len_needle:
        return -1

    i = 0
    while i <= len_haystack - len_needle:
        j = 0
        k = i
        print(f"starting {k=} {j=} {haystack[k]}")

        while j < len_needle and k < len_haystack and haystack[k] == needle[j]:
            print(f"Inside {k=} {j=} {haystack[k]}")
            j += 1
            k += 1

        if j == len_needle:
            return k - j

        print(f"after {k=} {j=} {haystack[k]}", end="\n---------\n")

        i += 1

    return -1


def str_str_chatgpt(haystack: str, needle: str) -> int:
    # Get the lengths of haystack and needle
    h_len = len(haystack)
    n_len = len(needle)

    # If needle is an empty string, return 0 (by problem definition)
    if n_len == 0:
        return 0

    # Loop through haystack, but only up to the point where the remaining characters can still match needle
    for i in range(h_len - n_len + 1):
        # Check if the substring of haystack starting at i matches needle
        if haystack[i : i + n_len] == needle:
            return i

    # If no match is found, return -1
    return -1




if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    print(str_str(haystack=haystack, needle=needle))
    print(str_str_inbuilt(haystack=haystack, needle=needle))

    haystack = "leetcode"
    needle = "leeto"
    print(str_str(haystack=haystack, needle=needle))
    print(str_str_inbuilt(haystack=haystack, needle=needle))

    haystack = "hello"
    needle = "ll"
    print(str_str(haystack=haystack, needle=needle))
    print(str_str_inbuilt(haystack=haystack, needle=needle))

    haystack = "a"
    needle = "a"
    print(str_str(haystack=haystack, needle=needle))
    print(str_str_inbuilt(haystack=haystack, needle=needle))

    haystack = "mississippi"
    needle = "issip"
    print(str_str(haystack=haystack, needle=needle))
    print(str_str_inbuilt(haystack=haystack, needle=needle))
