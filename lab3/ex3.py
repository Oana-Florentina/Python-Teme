#3. Compare two dictionaries without using the operator "=="
# returning True or False. (Attention, dictionaries must be recursively
# covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def recursive_dict_compare(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not recursive_dict_compare(value1, value2):
                return False
        elif value1 != value2:
            return False

    return True

dict1 = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
dict2 = {"a": 1, "b": {"c": 2, "d": [3, 4]}}
dict3 = {"a": 1, "b": {"c": 2, "d": [3, 5]}}

print(recursive_dict_compare(dict1, dict2))
print(recursive_dict_compare(dict1, dict3))  
