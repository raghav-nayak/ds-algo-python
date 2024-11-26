# https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150


# 322. Coin Change

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from typing import List

# def coin_change(coins: List[int], amount: int, count: int) -> int:
#     if amount <= 0:
#         return 0

#     # for index, value in enumerate(coins):
#     #     remainder = amount - value
#     #     remainder_result = coin_change(coins, remainder)
#     #     if remainder_result != 0:
#     #         remainder_result.append(value)
#     #         return len(remainder_result)
#     # return -1

#     for coin in coins:
#         if coin < amount:
#             coin_change(coins, amount - coin, count + 1)


def coin_change_chatgpt(coins: List[int], amount: int) -> int:
    # Initialize dp array with a large value
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0

    # Fill the dp array
    for amount_index in range(1, amount + 1):
        for coin in coins:
            remainder_amount = amount_index - coin
            if remainder_amount >= 0:
                dp[amount_index] = min(dp[amount_index], dp[remainder_amount] + 1)

    # Check if amount can be made up
    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coin_change_chatgpt(coins, amount))

    coins = [2]
    amount = 3
    print(coin_change_chatgpt(coins, amount))

    coins = [1]
    amount = 0
    print(coin_change_chatgpt(coins, amount))
