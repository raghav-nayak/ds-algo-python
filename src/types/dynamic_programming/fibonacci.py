def fibonacci(num: int) -> int:
    if num == 0:
        return 0

    if num == 1:
        return 1

    return fibonacci(num - 2) + fibonacci(num - 1)


def fibonacci_with_memo_impl(num: int, memo: list):
    if num <= 1:
        return num
    if memo[num] != 0:
        return memo[num]

    result = fibonacci_with_memo_impl(num - 2, memo) + fibonacci_with_memo_impl(
        num - 1, memo
    )
    memo[num] = result
    return result


def fibonacci_with_memo(num: int) -> int:
    memo = [0] * (num + 1)
    return fibonacci_with_memo_impl(num=num, memo=memo)


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(5))
    # print(fibonacci(50))
    print(fibonacci_with_memo(100))
