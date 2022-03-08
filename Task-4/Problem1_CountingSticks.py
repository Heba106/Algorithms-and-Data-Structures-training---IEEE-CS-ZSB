# CodeForces : Counting Sticks
if __name__ == "__main__":
    exp= input()
    plus = exp.index('+')  #find the signs indeces
    equal = exp.index('=')
    A= len(exp[0:plus])   #getting A , B , C 
    B= len(exp[plus+1:equal])
    C=len(exp[equal+1:])
    if A+B+1==C-1:        #ckeck if the expression can be obtained by moving one stick
        A+=1
        C-=1
    elif  A+B-1==C+1:
        if A>1 :
            A-=1 
        else :
            B-=1
        C+=1
    if A+B==C :           #printing results 
         print('{}+{}={}'.format('|'*(A),'|'*B,'|'*(C)))
    else: 
        print("Impossible")
        