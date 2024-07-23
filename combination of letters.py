from itertools import product

example_dict = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
    '3': ['e', 'f']
}

combinations = [''.join(comb) for comb in product(*example_dict.values())]

for combo in combinations:
    print(combo)
