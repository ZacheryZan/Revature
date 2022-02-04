""""""
def multiEleven(s):
    """"""
    dig = '0123456789'
    bCarry = False
    strBuild = ''
    strAddition = ''
    strM10 = s[::-1].zfill(len(s) + 1)
    strM1 = (s.zfill(len(s) + 1))[::-1]
    if s[0] == '9' and s[1] != '0':
        strM10 += '0'
        strM1 += '0'
    intLen = len(strM10)
    for num in range(0, intLen):
        strAddition = str(dig.find(strM10[num]) + dig.find(strM1[num]) + int(bCarry))
        strBuild += strAddition[-1]
        if len(strAddition) == 2:
            bCarry = True
        else:
            bCarry = False            
    print(strM10)
    print(strM1)
    print(''.zfill(intLen).replace('0', '-') + '\n', strBuild[::-1], sep='', end='')

print('multiEleven\n11')
multiEleven(input())
