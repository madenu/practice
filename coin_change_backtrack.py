# This is a constraint satisfaction problem
# https://leetcode.com/problems/coin-change/description/


class Solution:

    @staticmethod
    def coinChange(coins, amount) -> int:
        if amount == 0:
            return 0
        # Generate node-consistent domains
        domains = {coin: list(range(1, (amount // coin) + 1))[::-1] for coin in coins}
        return Solution._coin_change_backtrack(domains, {}, sorted(coins)[::-1], amount)

    @staticmethod
    def _coin_change_backtrack(domains, assignment, coins, amount) -> int:
        if not coins:
            total = sum([v for v in assignment.values()])
            return total if total == amount else -1

        for coin in coins:
            for val in domains[coin]:
                assignment.update({coin: val})
                total = sum([k * v for k, v in assignment.items()])
                if total > amount:
                    del assignment[coin]
                    continue
                elif total == amount:
                    # print(assignment)
                    return sum([v for v in assignment.values()])
                elif total < amount:
                    result = Solution._coin_change_backtrack(domains, assignment, coins[1:], amount)
                    if result >= 0:
                        return result

        return -1


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

    # TODO
    # coins = [1, 10, 25]
    # amount = 30
    # expected = 3
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected

    # TODO
    # coins = [186, 419, 83, 408]
    # amount = 6249
    # expected = 20
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
