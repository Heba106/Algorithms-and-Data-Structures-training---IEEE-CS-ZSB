import os
import random
import sys
import os

test = int(sys.argv[1]) #input no. of tests from cmd
n = int (sys.argv[2]) #input the parameter for the tests from cmd

for i in range (test) :
    print ("Test no. " + str(i))
    #run generator file with n and i (seed)
    os.system( "python Gen.py " + str(n) + "  " + str(i) + " > input.txt")
    os.system( "python maxPairWise.py < input.txt > maxPairWise.txt")
    os.system( "python maximum_pairwise_product.py < input.txt > maximum_pairwise_product.txt")
    
    with open('maxPairWise.txt') as f: maxPairWise = f.read()
    print ("Program1 ",maxPairWise)

    with open('maximum_pairwise_product.txt') as f: maximum_pairwise_product = f.read()
    print ("Program2 ",maximum_pairwise_product)

    if maximum_pairwise_product != maxPairWise :
        print("Error")
        break 