# CodeForces : Andryusha and Socks
if __name__ == "__main__":
    n = int(input())
    socks=[0]*n
    table=0
    max=0
    for i in input().split():
        i=int(i)
        if socks[i-1]==0:
            socks[i-1]+=1 
            table+=1
            if table > max:
                max=table
        else:
            table-=1
    print (max)
