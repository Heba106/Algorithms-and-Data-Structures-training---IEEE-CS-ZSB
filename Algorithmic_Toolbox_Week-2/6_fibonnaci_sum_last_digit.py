def fibLastDigit(x):
    f0,f1,f2=0,1,0
    if x<=1:
        return x
    for _ in range (x-1):
        f2= int((f0+f1)%10)
        f0,f1=f1,f2
    return f2

def fibSum(n):
    sum=0
    for _ in range(n+1):
        sum= int((sum+fibLastDigit(_))%10)
    return sum

if __name__ == "__main__":
    n=int(input())
    print(fibSum(n))

