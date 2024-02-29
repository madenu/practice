class CoinPath:
    def __init__(self, denoms=None):
        if denoms is None:
            denoms = []
        self._path = denoms
        self.hash = self.__hash__()

    @property
    def count(self):
        return len(self._path)

    @property
    def amount(self):
        return sum(self._path)

    @property
    def path(self):
        return list(self._path)

    def update(self, denom):
        self._path.append(denom)

    def __hash__(self):
        return int(self.__repr__())

    def __eq__(self, other):
        return self.hash == other.hash

    def __repr__(self):
        return "".join([repr(x) for x in sorted(self._path)])

    def __str__(self):
        return "|".join([str(v) for v in self._path])


class Solution:

    @staticmethod
    def coinChange(coins, amount) -> int:

        coins_sorted = list(sorted(coins))
        small_coin = coins_sorted[0]

        if amount < small_coin:
            return 0

        unvisited = [CoinPath([denom]) for denom in coins_sorted]  # Reverse! Reverse!
        while unvisited:
            curr_path = unvisited.pop()
            remainder = amount - curr_path.amount
            if curr_path.amount == amount:  # Found a path to amount
                # from collections import Counter
                # print(f"Solution found: {Counter(str(curr_path).split('|'))}")
                return curr_path.count
            elif curr_path.amount > amount:  # Amount exceeded
                continue
            elif remainder < small_coin:  # This path leads nowhere
                continue
            elif curr_path.amount < amount:  # Keep looking
                for denom in [c for c in coins_sorted if c <= remainder]:
                    new_path = CoinPath(curr_path.path + [denom])  # TODO Refactor so not instantiating every time
                    if not (new_path in unvisited):
                        unvisited.append(new_path)

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

    # coins = [186, 419, 83, 408]
    # amount = 6249
    # expected = 20
    # actual = sol.coinChange(coins, amount)
    # assert actual == expected
