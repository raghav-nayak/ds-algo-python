# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


from typing import List


# my version : partial
def max_profit(prices: List[int]) -> int:
    profit = 0
    start = -1
    end = -1
    total_prices = len(prices)

    if total_prices <= 1:
        return profit

    for day in range(1, total_prices):
        print(f"{day=} {prices[day]} : {start=} {end=}")
        if start == -1:
            if prices[day] > prices[day - 1]:
                start = prices[day - 1]
                end = prices[day]
            else:
                start = prices[day]
        else:
            if prices[day] > end:
                end = prices[day]

    print(f"Final {start=} {end=}")
    if not (start == -1 and end == -1):
        profit = end - start
        if profit < 0:
            profit = 0

    return profit


# chatgpt
def max_profit(self, prices: List[int]) -> int:
    min_price = float("inf")  # Initialize to a very high number
    max_profit = 0  # Initialize profit to 0

    for price in prices:
        if price < min_price:
            min_price = price  # Update minimum price if a lower price is found
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Update max profit

    return max_profit


if __name__ == "__main__":
    # prices = [7, 1, 5, 3, 6, 4]
    # print(f"{max_profit(prices=prices)}")

    # prices = [7, 6, 4, 3, 1]
    # print(f"{max_profit(prices=prices)}")

    # prices = [2, 1, 2, 0, 1]
    # print(f"{max_profit(prices=prices)}")

    # prices = [1, 2]
    # print(f"{max_profit(prices=prices)}")

    prices = [2, 1, 2, 1, 0, 1, 2]
    print(f"{max_profit(prices=prices)}")
