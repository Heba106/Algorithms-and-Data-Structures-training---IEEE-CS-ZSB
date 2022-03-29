def fibSumSquares(x):
    f0,f1,f2=0,1,0
    x%=60
    if x<=1:
        return x
    for _ in range (x-1):
        f2= int((f0+f1)%10)
        f0,f1=f1,f2 
    return ((f2*(f2+f0))%10)


if __name__ == "__main__":
    n=int(input())
    print(fibSumSquares(n))
