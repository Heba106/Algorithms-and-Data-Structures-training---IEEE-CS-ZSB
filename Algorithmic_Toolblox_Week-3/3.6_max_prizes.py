n = int(input())
i=1
lst=[]
while n>0:   
        if (n-i)> max(lst, default=-1) or n> lst[-1]:
            lst.append(i)
            n-=i
        else:
            lst[-1]+=n
            break
        i+=1

    

print(len(lst))
print(' '.join([str(i) for i in lst]))