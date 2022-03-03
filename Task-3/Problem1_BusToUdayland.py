# CodeForces : Bus to Udayland
if __name__ == "__main__":
    n = int(input())
    a=[]
    [a.append(input()) for _ in range(n)]
    flag='No'
    for i in range(n):
        if a[i][0]==a[i][1]=='O':
            flag='Yes'
            a[i]=('++'+a[i][2:5])
            break
        if a[i][3]==a[i][4]=='O':
            flag='Yes'
            a[i]=(a[i][0:3]+'++')
            break
    print(flag)
    if flag == 'Yes':
        [print(a[i]) for i in range(n)]



            