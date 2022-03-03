# CodeForces : Anton and Danik
if __name__ == "__main__":
    n = int(input())
    str=input()
    if str.count('A')>str.count('D'):
        print("Anton")
    elif str.count('A')<str.count('D'):
        print("Danik")
    else:
        print("Friendship")