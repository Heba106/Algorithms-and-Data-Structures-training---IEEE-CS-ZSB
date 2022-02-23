# BeeCrowd: Robot Basketball
if __name__ == '__main__':
    d=int(input())
    if d < 0 or d>2000:
        print("Invalid Input")
    elif d<=800:
        print(1)
    elif d <= 1400:
        print(2)
    else:
        print(3)