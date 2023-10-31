#1.Write a function that receives as parameters two lists a and b
# and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def set_operations(a, b):
    intersection = set(a) & set(b)

    union = set(a) | set(b)

    difference_a_minus_b = set(a) - set(b)

    difference_b_minus_a = set(b) - set(a)

    result = [intersection, union, difference_a_minus_b, difference_b_minus_a]
    return result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = set_operations(a, b)
print(result)
