
text=['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']

a=[]
for i in text:
    a.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))


print(''.join(a))
