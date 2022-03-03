# CodeForces:One-dimensional Japanese Crossword
if __name__ == "__main__":
    n = int(input())
    str=input()
    groupSize=[]
    size=0
    counter=0
    for i in str:
        if i =='W':
            if size!=0: groupSize.append(size)
            size=0
        else:
            if size==0:
                counter+=1
                size+=1
            else:
                size+=1
    if size!=0:
        groupSize.append(size) 
    print(counter)
    if groupSize!=[]: print(*groupSize, sep=' ')
