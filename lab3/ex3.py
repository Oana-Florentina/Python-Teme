# 3. Compare two dictionaries without using the operator "=="
# returning True or False. (Attention, dictionaries must be recursively
# covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def recursive_dict_compare(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, (dict, list, set)) and isinstance(value2, (dict, list, set)):
            # am lista sau dictionar:
            if not recursive_compare(value1, value2):
                return False
        else:
            if value1 != value2:
                return False

    return True


def recursive_compare(obj1, obj2):
    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        return recursive_dict_compare(obj1, obj2)

    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for item1, item2 in zip(obj1, obj2):
            if not recursive_compare(item1, item2):
                return False
        return True

    return obj1 == obj2


dict1 = {"a": 1,
         "b": {"c": 2, "d": [3, 4]}}
dict2 = {"a": 1,
         "b": {"c": 2, "d": [3, 4]}}
dict3 = {"a": 1,
         "b": {"c": 2, "d": [3, 5]}}

print(recursive_compare(dict1, dict2))  # True
print(recursive_compare(dict1, dict3))  # False



