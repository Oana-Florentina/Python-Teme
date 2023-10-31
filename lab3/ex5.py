# 5. The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values)
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.
def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False

        value = dictionary[key]
        if (
            (not prefix or value.startswith(prefix)) and
            (not suffix or value.endswith(suffix)) and
            (middle in value and value.find(middle) != 0 and value.rfind(middle) != len(value) - len(middle))
        ):
            continue
        else:
            return False

    return True


# Example usage:
validation_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
user_data = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}

result = validate_dict(validation_rules, user_data)
print(result)  # Should print False
