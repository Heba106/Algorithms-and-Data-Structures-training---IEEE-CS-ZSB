# CodeForces : Colorful Stones
if __name__ == "__main__":
    s,t =input() , input()
    position=0
    for i in t :
        if i==s[position]:
            position+=1
    print(position+1)