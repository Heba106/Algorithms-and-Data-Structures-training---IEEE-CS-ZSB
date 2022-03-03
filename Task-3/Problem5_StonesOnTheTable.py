# CodeForces : Stones on the Table
if __name__ == "__main__":
    n = int(input())
    s=input()
    counter=0
    for i in range(len(s)):
        if i !=0:
            if s[i]==s[i-1]:
                counter+=1
    print (counter)
