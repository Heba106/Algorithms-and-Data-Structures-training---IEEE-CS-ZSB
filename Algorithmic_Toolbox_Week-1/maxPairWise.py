def maxProduct(arr):
    a=0
    b=0
    n=len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]; b = arr[j]
 
    return a*b
if __name__ == "__main__":
    n = int(input())
    arr= list(map(int,input().split()))
    print(maxProduct(arr))