from itertools import zip_longest

def combine_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    combined_tuples = []

    for i in range(max_length):
        tuple_items = tuple(lst[i] if i < len(lst) else None for lst in lists)
        combined_tuples.append(tuple_items)

    return combined_tuples


list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b"]

result = combine_lists(list1, list2, list3)
print(result)
