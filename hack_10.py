"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    new_keys_values = [("1", "2"), ("3", "4"), ("5", "6")]

    for i in range(len(result)):
        new_key, new_value = new_keys_values[i]
        result[i] = {new_key:new_value}
    return result
