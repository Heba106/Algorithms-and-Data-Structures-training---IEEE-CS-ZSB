# CodeForces : Mishka and Contest
if __name__ == "__main__":
    n,k= list(map(int,input().split()))
    a = list(map(int, input().split()))
    result=0
    while len(a)>0:
        if a[0]<=k:
            result+=1
            del a[0]
        elif a[-1]<=k:
            result+=1
            del a[-1]
        else:
            break
    print(result)