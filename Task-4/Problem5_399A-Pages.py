# CodeForces : 399A- Pages
if __name__ == "__main__":
    n,p,k= list(map(int,input().split()))
    result=[]
    if p-k>1:
        result.append("<<")
    for x in range (p-k,p+k+1,1):
        if x>=1 and x<=n:
                result.append(str(x))
    if int(result[-1])<n: result.append(">>")
    result[result.index(str(p))]="({})".format(p)
    print(" ".join(result))
