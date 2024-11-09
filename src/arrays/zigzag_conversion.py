# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000


def convert_chatgpt(s: str, numRows: int) -> str:
    # Edge case: If only one row or fewer rows than string length, return original string
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize an array of empty strings for each row
    rows = [str()] * numRows
    current_row = 0
    going_down = False

    # Populate the rows list with zigzag pattern
    for char in s:
        rows[current_row] += char
        # Change direction at the top and bottom rows
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Move up or down based on the direction
        current_row += 1 if going_down else -1

    # Join all rows to form the final zigzagged string
    return "".join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert_chatgpt(s, numRows))

    s = "PAYPALISHIRING"
    numRows = 4
    print(convert_chatgpt(s, numRows))

    s = "A"
    numRows = 1
    print(convert_chatgpt(s, numRows))
