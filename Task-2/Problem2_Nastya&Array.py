# CodeForces: Nastya and an Array
if __name__ == "__main__":
    n = int(input())
    arr=list(map(int, input().split()))
    arr = [i for i in arr if i != 0]
    arr=set(arr)
    print(len(arr))