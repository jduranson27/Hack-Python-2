"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    list = []
    
    if not result:
        return ['0']
    
    for i in range(len(result)):
        if (i+1) % 2 !=0:
            list.append(str(i+1))
        elif (i+1) % 2 == 0:
            list.append('-')    

    result = list
    return result
