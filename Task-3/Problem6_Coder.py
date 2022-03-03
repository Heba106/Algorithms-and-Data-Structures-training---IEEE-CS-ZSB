# CodeForces : Coder
if __name__ == "__main__":
    n = int(input())
    if n%2==0:
        print(int((n*n)/2))
    else:
        print(int((n*n+1)/2))
    arr1 = []
    for i in range(n):
        arr2 = []
        for j in range(n):
            if (i + j) % 2 == 0:
                arr2.append("C")
            else:
                arr2.append(".")
        arr1.append(arr2)
    for n in arr1:
        print("".join(n))