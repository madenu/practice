# This is a constraint satisfaction problem
# https://leetcode.com/problems/coin-change/description/


class Solution:

    @staticmethod
    def coinChange(coins, amount) -> int:
        if amount == 0:
            return 0

        coins = sorted(set(coins))

        # Generate node-consistent domains
        domains = {coin: list(range(1, (amount // coin) + 1)) for coin in coins}

        # Generate arc-consistent domains
        stack = []
        for ii in range(len(coins)):
            for jj in range(ii + 1, len(coins)):
                stack.append((coins[ii], coins[jj]))

        while stack:
            coin_i, coin_j = stack.pop()
            if Solution._revise(domains, coin_i, coin_j):
                if len(domains[coin_i]) == 0:
                    return -1
                for neighbor in set(coins) - {coin_j}:
                    stack.append((coin_i, neighbor))

        # Search the space for a solution
        visited = set()
        for coin in coins[::-1]:
            assignments = [((coin, reps),) for reps in domains[coin]]

            while assignments:
                assignment = assignments.pop()
                if assignment in visited:
                    continue

                source_amt = sum([c * r for c, r in assignment])
                visited.add(assignment)
                if source_amt > amount:
                    continue
                elif source_amt == amount:
                    return sum([r for c, r in assignment])
                elif source_amt < amount:
                    for neighbor_coin in sorted(set(coins) - {coin})[::-1]:
                        adjacent = []
                        for reps in domains[neighbor_coin]:
                            adjacent.append(assignment + ((neighbor_coin, reps),))
                        assignments.extend(adjacent)

        return -1

    @staticmethod
    def _revise(domains, coin_i, coin_j):
        revised = True
        for reps_i in domains[coin_i]:
            for reps_j in domains[coin_j]:
                if coin_i * reps_i + coin_j + reps_j <= amount:
                    revised = False
            if revised:
                domains[coin_i].remove(reps_i)
                return revised

        return revised


if __name__ == "__main__":
    sol = Solution()

    # coins = [1, 2, 5]
    # amount = 11
    # expected = 3
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
    #
    # coins = [2]
    # amount = 3
    # expected = -1
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
    #
    # coins = [1]
    # amount = 0
    # expected = 0
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
    #
    # coins = [1, 2, 5]
    # amount = 100
    # expected = 20
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected

    coins = [186, 419, 83, 408]  # TODO Try a backtracking algorithm
    amount = 6249
    expected = 20
    actual = sol.coinChange(coins, amount)
    assert actual == expected
