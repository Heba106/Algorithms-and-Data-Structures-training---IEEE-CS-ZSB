def gcd(a,b):
    if b==0:
        return a
    else:
        anew =a%b
        return gcd(b,anew)

if __name__ == "__main__":
    c,d= list(map(int,input().split()))
    print(gcd(c,d))