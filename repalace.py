def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i 
    return result

text = "Py hon"
ch = "t"

print(str_replace(text,ch))