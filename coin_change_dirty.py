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
        return self.__repr__()


def coin_change(coins, amount):
    if amount == 0:
        return 0

    small_count = float('inf')
    small_coin = min(coins)
    unvisited = [CoinPath([denom]) for denom in coins]
    candidates = []
    visited = []

    while unvisited:
        curr_path = unvisited.pop()
        leftover = amount - curr_path.amount
        if curr_path.count < small_count:
            if curr_path.amount == amount:  # Found a path to amount
                candidates.append(curr_path)
                small_count = curr_path.count
                continue
            elif curr_path.amount > amount:  # Amount exceeded
                continue
            elif leftover < small_coin:  # This path leads nowhere
                continue
            elif curr_path.amount < amount:  # Keep looking
                for denom in [c for c in coins if c <= leftover]:
                    new_path = CoinPath(curr_path.path + [denom])  # TODO Refactor so not instantiating every time
                    if not (new_path in visited):
                        visited.append(new_path)
                        unvisited.append(new_path)

    result = -1
    if candidates:
        result = min([c.count for c in candidates])

    return result


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    expected = 3
    actual = coin_change(coins, amount)
    assert actual == expected

    coins = [2]
    amount = 3
    expected = -1
    actual = coin_change(coins, amount)
    assert actual == expected

    coins = [1]
    amount = 0
    expected = 0
    actual = coin_change(coins, amount)
    assert actual == expected

    coins = [1, 2, 5]
    amount = 100
    expected = 20
    actual = coin_change(coins, amount)
    assert actual == expected

    coins = [186,419,83,408]
    amount = 6249
    print(coin_change(coins, amount))
