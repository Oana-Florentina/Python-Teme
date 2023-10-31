# 7. Write a function that receives a variable number of sets and returns a
# dictionary with the following operations from all sets two by two: reunion,
# intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.

def set_operations(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            # Union
            key_union = f"{set1} | {set2}"
            result[key_union] = set1 | set2

            # Intersection
            key_intersection = f"{set1} & {set2}"
            result[key_intersection] = set1 & set2

            # Difference (a - b)
            key_diff_ab = f"{set1} - {set2}"
            result[key_diff_ab] = set1 - set2

            # Difference (b - a)
            key_diff_ba = f"{set2} - {set1}"
            result[key_diff_ba] = set2 - set1

    return result


set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)

for key, value in result.items():
    print(f"{key}: {value}")
