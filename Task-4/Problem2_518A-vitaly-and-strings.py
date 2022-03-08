# CodeForces : 518A Vitaly And Strings
import sys
s=list(input())
t=list(input())
for i in range (len(s)-1,-1,-1):
    while s[i]!='z':
        s[i]=chr(ord(s[i])+1)
        if s<t :
            print(''.join(s))
            sys.exit()
    if s[i]=='z':
        s[i]='a'
print("No such string")

            