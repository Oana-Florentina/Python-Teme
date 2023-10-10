def set_operations(a, b):
    
    set_a = set(a)
    set_b = set(b)

    intersection = list(set_a.intersection(set_b))
    union = list(set_a.union(set_b))
    a_minus_b = list(set_a.difference(set_b))
    b_minus_a = list(set_b.difference(set_a))

    return intersection, union, a_minus_b, b_minus_a


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
intersection, union, a_minus_b, b_minus_a = set_operations(list_a, list_b)

print("Intersection:", intersection)
print("Union:", union)
print("A - B:", a_minus_b)
print("B - A:", b_minus_a)
