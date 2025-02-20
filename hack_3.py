"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    reemplazo={'a':'@', 'e':'3', 'i':'¡', 'o':'0', 'u':'v'}
    ls=[]
    result=result.capitalize()

    for txt in result:
        if txt in reemplazo:
            ls.append(reemplazo[txt])
        else:
            ls.append(txt)
        
    result= ''.join(ls)
    if result[-1] in reemplazo.values():
        return result
    else:
        result = result[:-1] + result[-1].upper()
    return result