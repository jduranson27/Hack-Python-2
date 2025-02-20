"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    if len(s) > 3:
        result = s[1:]
        if len(result) > 5:
            result = result[:-1]
    else:
        result = s
    return result