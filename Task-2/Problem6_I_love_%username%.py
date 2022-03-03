# CodeForces : I_love_%username%
if __name__ == "__main__":
    n = int(input())
    arr=[]
    counter=0
    for i in input().split():
        i=int(i)
        if i not in arr:
            arr.append(i)
            if len(arr)>1:
                if i is max(arr) or i is min(arr):
                    counter+=1
    print(counter)
    