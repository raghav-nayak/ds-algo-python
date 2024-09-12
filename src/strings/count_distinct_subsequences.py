# Given a string, find the count of distinct subsequences of it.

# Examples:
# Input: str = “gfg”
# Output: 7
# Explanation: The seven distinct subsequences are “”, “g”, “f”, “gf”, “fg”, “gg” and “gfg”

# Input: str = “ggg”
# Output: 4
# Explanation: The four distinct subsequences are “”, “g”, “gg” and “ggg”


def count_distinct_subsequences(input_str: str):
    input_str_len = len(input_str)
    distinct_patterns = [0] * (input_str_len + 1)
    distinct_patterns[0] = 1  # Empty subsequence

    last_occurrence = {}

    for i in range(1, input_str_len + 1):
        distinct_patterns[i] = 2 * distinct_patterns[i - 1]

        # If the character has appeared before, subtract the subsequences
        # formed before its last occurrence to avoid duplicates.
        if input_str[i - 1] in last_occurrence:
            distinct_patterns[i] -= distinct_patterns[
                last_occurrence[input_str[i - 1]] - 1
            ]

        # Update the last occurrence of the current character.
        last_occurrence[input_str[i - 1]] = i

    return distinct_patterns[input_str_len]


if __name__ == "__main__":
    input_str = "gfg"
    print(f"{count_distinct_subsequences(input_str=input_str)}")

    input_str = "ggg"
    print(f"{count_distinct_subsequences(input_str=input_str)}")
