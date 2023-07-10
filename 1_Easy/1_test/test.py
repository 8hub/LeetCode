str1 = "globalna"

def updateString(string1):
    return string1 + "x"


def updateString2(str2):
    str2 = str2 + "xxx"
    print(str2)
    return str2

print(str1)
str1 = updateString2(str1)
print(str1)