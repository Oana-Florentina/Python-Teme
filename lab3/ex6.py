# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the
# number of duplicate elements in the list (use sets to achieve this objective).

def count_unique_and_duplicates(input_list):
    unique_elements = set()
    duplicate_elements = set()

    for item in input_list:
        if item in unique_elements:
            duplicate_elements.add(item)
        else:
            unique_elements.add(item)

    return len(unique_elements), len(duplicate_elements)


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_count, duplicate_count = count_unique_and_duplicates(my_list)
print(f"Number of unique elements: {unique_count}")
print(f"Number of duplicate elements: {duplicate_count}")
