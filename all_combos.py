# This can get surprisingly complicated
# See https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n

def _all_combos(domains, sofar, order, *nums):
    if not nums:
        print(sofar)
        return

    for val in domains[nums[order]]:
        _all_combos(domains, sofar + [val], order - 1, *(nums[:order]))


def all_combos(domains, *nums):
    _all_combos(domains, [], len(nums) - 1, *nums)


if __name__ == '__main__':
    # ['x', 'a', 0]
    # ['x', 'a', 1]
    # ['x', 'b', 0]
    # ['x', 'b', 1]
    # ['y', 'a', 0]
    # ['y', 'a', 1]
    # ['y', 'b', 0]
    # ['y', 'b', 1]
    print(all_combos({0: [0, 1], 1: ['a', 'b'], 2: ['x', 'y']}, 0, 1, 2))

    coins = [5, 10, 25]
    amount = 100
    domains = {coin: list(range(1, (amount // coin) + 1)) for coin in coins}
    print(all_combos(domains, *coins))
