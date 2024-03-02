# This is a constraint satisfaction problem
# https://leetcode.com/problems/coin-change/description/


class Solution:

    def coinChange(self, coins, amount) -> int:
        dp = [0] + [float('inf') for _ in range(1, amount + 1)]  # dp[i] = Fewest coins needed to total amount i
        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1


if __name__ == "__main__":
    sol = Solution()

    coins = [1, 2, 5]
    amount = 11
    expected = 3
    actual = sol.coinChange(coins, amount)
    assert actual == expected

    coins = [2]
    amount = 3
    expected = -1
    actual = sol.coinChange(coins, amount)
    assert actual == expected

    coins = [1]
    amount = 0
    expected = 0
    actual = sol.coinChange(coins, amount)
    assert actual == expected

    coins = [1, 2, 5]
    amount = 100
    expected = 20
    actual = sol.coinChange(coins, amount)
    assert actual == expected

    coins = [1, 10, 25]
    amount = 30
    expected = 3
    actual = sol.coinChange(coins, amount)
    assert actual == expected

    coins = [186, 419, 83, 408]
    amount = 6249
    expected = 20
    actual = sol.coinChange(coins, amount)
    assert actual == expected
