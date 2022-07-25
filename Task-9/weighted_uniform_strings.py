# HckerRank Weighted Uniform String
def weightedUniformStrings(s,queries):
    result=[]
    # to store the weights 
    d={}
    weight=0
    for i in range(len(s)):
        if i==0 or s[i]!=s[i-1]:
            weight = ord(s[i])-ord('a')+1
        else:
            weight = weight + ord(s[i])-ord('a') + 1
        d[weight]=1
    
    for q in queries:
        result.append('Yes' if q in d else 'No')
    return result


if __name__ == "__main__":
    s= input()
    queries= list(map(int,input().strip().split()))
    print(weightedUniformStrings(s, queries))
