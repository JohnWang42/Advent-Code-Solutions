import re

def toCode(text):
    codeArr = []
    for char in text:
        codeArr.append(ord(char))
    return codeArr

def toText(arr):
    newPass = ''
    for code in arr:
        newPass += chr(code)
    return newPass

def genPass(start):
    passArr = toCode(start)
    match = False
    while not match:
        for i in reversed(range(0, 8)):
            if passArr[i] < ord('z'):
                passArr[i] += 1
                break
            else:
                passArr[i] = ord('a')
        newPass = toText(passArr)
        if 'i' in newPass or 'o' in newPass or 'l' in newPass:
            continue
        check = re.findall(ur'([a-z])(\1)', newPass)
        if len(check) < 2:
            continue
        for i in range(0, 6):
            if passArr[i] + 1 == passArr[i + 1] and passArr[i] + 2 == passArr[i + 2]:
                match = True
                break
    return toText(passArr)

answer1 = genPass('hepxcrrq')
print answer1
print genPass(answer1)
