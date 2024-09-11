# https://www.geeksforgeeks.org/check-two-strings-k-anagrams-not/
#
# Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.

# Two strings are called k-anagrams if following two conditions are true.
#     1. Both have same number of characters.
#     2. Two strings can become anagram by changing at most k characters in a string.

# Examples:
# 1. Input:  str1 = "anagram" , str2 = "grammar" , k = 3
# Output:  Yes
# Explanation: We can update maximum 3 values and
# it can be done in changing only 'r' to 'n'
# and 'm' to 'a' in str2.

# 2. Input:  str1 = "geeks", str2 = "eggkf", k = 1
# Output:  No
# Explanation: We can update or modify only 1
# value but there is a need of modifying 2 characters.
# i.e. g and f in str 2.


from collections import defaultdict


## Brute Force
# time complexity: O(n)
# space complexity: O(n)
def is_k_anagram_brute_force(str1, str2, k):

    if len(str1) != len(str2):
        return False

    count_map = defaultdict(int)

    for char in str1:
        count_map[char] += 1

    for char in str2:
        if count_map[char] > 0:
            count_map[char] -= 1

    diff_count = sum(count_map.values())

    return True if diff_count <= k else False


## optimized
def is_k_anagram_optimized(str1, str2, k):
    MAX_CHAR = 26
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len != str2_len:
        return False

    hash_str1 = [0] * MAX_CHAR
    for i in range(str1_len):
        hash_str1[ord(str1[i]) - ord("a")] += 1

    print(f"{hash_str1=}")
    count = 0
    for i in range(str1_len):
        if hash_str1[ord(str2[i]) - ord("a")] > 0:
            hash_str1[ord(str2[i]) - ord("a")] -= 1
        else:
            count += 1

    print(f"{hash_str1=}")

    if count > k:
        return False

    return True


if __name__ == "__main__":
    str1 = "anagram"
    str2 = "grammar"
    k = 3

    print(f"{str1=} {str2=} {k=} is_anagram={is_k_anagram_brute_force(str1, str2, k)}")
    print(f"{str1=} {str2=} {k=} is_anagram={is_k_anagram_optimized(str1, str2, k)}")

    str1 = "geeks"
    str2 = "eggkf"
    k = 1

    print(
        f"\n\n{str1=} {str2=} {k=} is_anagram={is_k_anagram_brute_force(str1, str2, k)}"
    )
    print(f"{str1=} {str2=} {k=} is_anagram={is_k_anagram_optimized(str1, str2, k)}")
