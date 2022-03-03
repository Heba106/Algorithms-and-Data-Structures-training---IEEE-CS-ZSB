# CodeForces: Sereja and Dima
if __name__ == "__main__":
    n = int(input())
    arr=list(map(int, input().split()))
    Sereja=Dima=0
    while len(arr)>0:
        Sereja+= arr.pop(arr.index(max(arr[0],arr[-1])))
        if len(arr)>0:
            Dima+= arr.pop(arr.index(max(arr[0],arr[-1])))
    print(Sereja , Dima)