def fib(n):
    f0,f1,f2=0,1,0
    if n<=1:
        return n
    for _ in range (n-1):
        f2= f0+f1
        f0,f1=f1,f2
    return f2
    
if __name__ == "__main__":
    n=int(input())
    print(fib(n))