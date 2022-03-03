# CodeForces :  Beautiful Matrix
if __name__ == "__main__":
    mat=[]
    swaps=0
    for i in range (5):
        mat.append(list(map(int, input().split())))
    for i in range (5):
        for j in range (5):
            if mat[i][j]==1:
                swaps= abs(i-2)+abs(j-2)
                break
    print (swaps)
            
