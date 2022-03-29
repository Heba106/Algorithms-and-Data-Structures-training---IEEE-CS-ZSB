def fibLastDigit(x):
    f0,f1,f2=0,1,0
    if x<=1:
        return x
    for _ in range (x-1):
        f2= int((f0+f1)%10)
        f0,f1=f1,f2
    return f2

def fibPartialSum(m,n):
    sum=0
    for i in range(m,n+1):
        sum= int((sum+fibLastDigit(i))%10)
    return sum

if __name__ == "__main__":
    m,n= list(map(int,input().split()))
    print(fibPartialSum(m,n))

