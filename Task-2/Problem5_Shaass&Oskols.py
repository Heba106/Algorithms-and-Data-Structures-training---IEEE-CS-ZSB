# CodeForces : Shaass and Oskols
if __name__ == "__main__":
    i = int(input())
    a = list(map(int,input().strip().split()))[:i]
    m = int(input())
    for _ in range(m):
        x,y= list(map(int,input().split()))
        x-=1
        if x+1 < len(a):   
            a[x+1]+= a[x]-y
        if x > 0:
            a[x-1]+= y-1
        a[x]= 0
    for j in a:
        print(j)