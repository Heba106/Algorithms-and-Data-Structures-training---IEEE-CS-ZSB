# CodeForces: Brain's Photos
import sys
r,c = list(map(int,input().split()))
matrix=[list(map(str,input().strip().split()))[:c] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if matrix[i][j] in ['C','M','Y']:
            print("#Color")
            sys.exit()
print("#Black&White")