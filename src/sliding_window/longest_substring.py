# Given a string s, find the length of the longest substring without repeating characters.
# Input: “ABCBC”
# Output: 3
# Explanation: The longest substring without repeating characters is “ABC”

# Input: “AAA”
# Output: 1
# Explanation: The longest substring without repeating characters is “A”

# Input: “GEEKSFORGEEKS”
# Output: 7
# Explanation: The longest substrings without repeating characters are “EKSFORG” and “KSFORGE”, with lengths of 7.


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
        print(f"{input_str[end]} : {start=} {end=} {last_index[ord(input_str[end])]}")
        start = max(start, last_index[ord(input_str[end])] + 1)
        result = max(result, end - start + 1)
        last_index[ord(input_str[end])] = end
        print(f"{start=} {result=} last_index={last_index[ord(input_str[end])]}\n")

    return result


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
