# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def is_valid_parentheses(s: str) -> bool:
    s_len = len(s)
    if s_len <= 1:
        return False

    # '(', ')', '{', '}', '[' and ']'
    in_sym = ["(", "{", "["]
    index = 0
    stack = list()
    while index < s_len:
        char = s[index]
        if char in in_sym:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            pop_char = stack.pop()
            if (
                (pop_char == "(" and char != ")")
                or (pop_char == "[" and char != "]")
                or (pop_char == "{" and char != "}")
            ):
                return False
        index += 1
    return len(stack) == 0


if __name__ == "__main__":
    s = "()"
    print(f"{is_valid_parentheses(s)}")

    s = "()[]{}"
    print(f"{is_valid_parentheses(s)}")

    s = "(]"
    print(f"{is_valid_parentheses(s)}")
