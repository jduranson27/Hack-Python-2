# HACK PYTHON 2

### Estudiante Jean Duranson 

## 🏆 H-1
🎬 Cómo resolver el hack y adicional ejecutar el testing, para validar el hack.

![](https://github.com/SocialOplesk/hack_python_2/blob/main/hack_python_2_run_gif.gif)


```sh
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 

-----------------
⚡ example script

def fn_hack_1(s):
    result = s
    _ls = []

    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_ls:
       if len(txt) % 2 != 0:
          content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
          _ls.append(content)
       else:
          _ls.append(txt)    
    result = "".join(_ls)
    return result
```

## 🏆 H-2
```sh
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx"

-----------------
⚡ example script

def fn_hack_2(s):
    result = s
    vowels = ["a","e","i","o","u"]
    _str = []
    
    for txt in result:
        if txt not in vowels:
          _str.append(txt)  
          
    result = "".join(_str)
    return result   
```

## 🏆 H-3
```sh
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
```

## 🏆 H-4
```sh
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
```

## 🏆 H-5
```sh
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
```

## 🏆 H-6 (FOR)
```sh
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
```
<br/>

## 🏆 H-7 (WHILE)
```sh
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
```
<br/>

## 🏆 H-8
```sh
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
```
<br/>

## 🏆 H-9 (FOR)
```sh
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
```
<br/>

## 🏆 H-10
```sh
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
```
<br/>

