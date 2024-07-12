from collections import Counter

def combine_dicts(d1, d2):
    counter = Counter(d1)
    for key, value in d2.items():
        counter[key] += value
    return counter


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}


combined_dict = combine_dicts(d1, d2)


print("Sample Output:", combined_dict)
