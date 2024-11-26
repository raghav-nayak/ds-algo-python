# Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down or right.

# In how many ways can you travel to the goal on a grid with dimensions m * n?

# write a function gridTraveler(m, n) that calculates this


def grid_traveler(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def grid_traveler_with_memo_impl(m: int, n: int, memo: dict) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    if result := memo.get(f"{m},{n}"):
        return result

    memo[f"{m},{n}"] = grid_traveler_with_memo_impl(
        m - 1, n, memo
    ) + grid_traveler_with_memo_impl(m, n - 1, memo)
    return memo[f"{m},{n}"]


def grid_traveler_with_memo(m: int, n: int) -> int:
    memo = dict()
    return grid_traveler_with_memo_impl(m, n, memo=memo)


if __name__ == "__main__":
    print(grid_traveler(1, 1))
    print(grid_traveler(2, 3))
    print(grid_traveler(3, 2))
    # print(grid_traveler(50, 50))

    print(grid_traveler_with_memo(1, 1))
    print(grid_traveler_with_memo(2, 3))
    print(grid_traveler_with_memo(3, 2))
    print(grid_traveler_with_memo(50,50))
