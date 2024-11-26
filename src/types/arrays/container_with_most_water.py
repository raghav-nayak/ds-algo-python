# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1


# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List

def max_area(height: List[int]) -> int:
    if not height:
        return 0
    if len(height) == 1:
        return height[0]

    start = 0
    end = 1
    max_area = -1
    while end < len(height):
        start_height = height[start]
        end_height = height[end]
        area = min(start_height, end_height) * (end - start)
        if area > max_area:
            max_area = area
            start = start + 1
        else:
            end = end + 1

    return max_area

def max_area_corrected_version_by_chatgpt(height: List[int]) -> int:
    if not height or len(height) < 2:
        return 0

    start = 0
    end = len(height) - 1
    max_area = 0

    while start < end:
        start_height = height[start]
        end_height = height[end]

        max_area = max(max_area, (min(start_height, end_height) * (end-start)))

        if start_height < end_height:
            start += 1
        else:
            end -= 1

    return max_area

def max_area_best_soln_leetcode(self, height: List[int]) -> int:
    res, cur, p = 0, 0, max(height)
    l, r = 0, len(height) - 1
    while l < r:
        cur = (r - l) * min(height[l], height[r])
        if cur > res:
            res = cur
        elif height[r] > height[l]:
            l += 1
        else:
            r -= 1
        if (r - l) * p < res:
            break
    return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(max_area(height))
