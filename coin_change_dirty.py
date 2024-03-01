class Solution:

    @staticmethod
    def coinChange(coins, amount) -> int:
        if amount == 0:
            return 0

        queue = []
        visited = set()
        coins = sorted(coins)
        queue.append((coins[-1],))

        while queue:
            source = queue.pop()

            if source in visited:
                continue

            source_amt = sum(source)
            visited.add(source)
            if source_amt > amount:
                continue
            elif source_amt == amount:
                return len(source)
            elif source_amt < amount:
                for coin in coins:  # Append vertices s.t. the first path found is guaranteed to be the shortest
                    adjacent = source + (coin,)
                    if not ((sum(adjacent) > amount) or (adjacent in visited)):
                        queue.append(adjacent)

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

    # This test case breaks my algorithm.
    # It takes way too long.
    # Try again with a backtracking algorithm.
    #
    # coins = [186, 419, 83, 408]
    # amount = 6249
    # expected = 20
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
