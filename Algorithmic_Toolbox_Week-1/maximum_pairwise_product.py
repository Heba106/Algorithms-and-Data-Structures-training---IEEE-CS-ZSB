def max_pairwise_product(a):
    a=sorted(a);
    return a[-1]*a[-2]
if __name__ == "__main__":
    n = int(input())
    arr= list(map(int,input().split()))
    print(max_pairwise_product(arr))