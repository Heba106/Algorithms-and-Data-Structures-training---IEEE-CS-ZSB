# Uses python3
def get_change(m):
    m = (m//10)+((m%10)//5)+(m%5)
    return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))