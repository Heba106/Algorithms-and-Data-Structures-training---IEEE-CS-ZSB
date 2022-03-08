# CodeForces : 105A Transmigration
if __name__ == "__main__": 
    n,m,k=map(float,input().split())
    n,m,k=int(n),int(m), round(k,3)
    skills={}
    for i in range (n):
        a=input().split()
        level= (int(a[1])*k)
        if level>=100:
            skills.update({a[0]:round(level)})
    for i in range (m):
        a=input()
        if a not in skills:
            skills.update({a:0})
    skills=sorted(skills.items())
    print(len(skills))
    [print(key , value) for key , value in skills]
