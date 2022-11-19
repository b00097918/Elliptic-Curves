from re import S


Values = "label" #label is the given string
flag = ""

for i in Values:
    flag += chr(ord(i) ^ 13)

    print(f"crypto{{{flag}}}") #The flag is then out putted in python f-strings