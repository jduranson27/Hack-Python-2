"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    list = []
    
    conten = len(result)
    
    if conten % 2 !=0:
        for i in range(len(result)):
            list.append(f'{result[i]}-{i+1}')        
    else:
        for i in range(len(result)):
            list.append(str(i+1))
        
    result = list
    result.reverse()
    return result
