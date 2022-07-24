def max_dot_product(a, b):
    # list.sort(reverse=True)
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n = int(input())
    b = list(map(int,input().strip().split()))[:n]
    a = list(map(int,input().strip().split()))[:n]
    print(max_dot_product(a, b))
    
