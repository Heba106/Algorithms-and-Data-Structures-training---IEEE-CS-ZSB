def pisano(divisor):
    fib=[0,1]
    while True :
        fib.append((fib[-1]+fib[-2])%divisor)
        if fib[-1]==1 and fib[-2]==00 :
            return fib[:-2]
def F_mod_m(n,m):
    fib=pisano(m)       
    n%=len(pisano(m))
    return fib[n]
if __name__ == "__main__":
    n,m= list(map(int,input().split()))
    print(F_mod_m(n,m))
