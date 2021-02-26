"""Examples of list and loop algorithms"""

def sum_algo(xs: list[int]) -> int:
    """Summation of input list is returned"""
    # 1. Initialize total and index i to 0
    total: int = 0
    i: int = 0
    # 2. While i is valid, meaning i < len(xs)
    while i < len(xs):
        #   2. True) Take xs[i] and add to the total
        total += xs[i]
        #   2. True) Increase i by 1, moving it to the next index
        i += 1
    # 2. False) Reslut os stored in totoal variable
    return total


# Example usage of the sum_algo function
    """odds: list[int] = [1, 3, 5, 7]
    odds_sum: int = sum_algo(odds)
    print(odds_sum)"""

#diagramming example
single: list[int] = [110]
many: list[int] = [1, 3, 5]
print(sum_algo(single))
print(sum_algo(many))