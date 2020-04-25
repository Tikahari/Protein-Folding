from Debug import *
import random
import sys
import math

directions = ["L", "R", "F"]
# ["A",   "C",    "I",    "L"   ,    "M"   ,    "F"   ,    "P"   ,
#     "W"   ,    "Y"   ,    "V" ,    "R"  ,    "N"  ,    "D"  ,    "Q"  ,
#     "E"  ,    "G"  ,    "H",    "K",    "S",    "T" ]

# seq = protein seq ; prob = mutation prob
def mutate(pop,prob):
    mut_pop=[]
    for p in range(len(pop)):
        seq=pop[p]
        # get random protein to switch
        x = random.randint(0, 2) 
        sequence=[]
       
        for i in range(len(seq)):
            rand= random.random()
            if(rand<=prob):
                r2=random.random() *2
                if(r2>=1):
                    x = random.randint(0, 2) 
                    # mutate
                    if(directions[x]!= seq[i]):
                        sequence.append(directions[x])
                # else:
                # delete do nothing
                    
            else:
                sequence.append(seq[i])
        # print("sequence is "+ sequence)
        # print()
        mut_pop.append(sequence)
        
    return mut_pop

# z=[['L', 'F', 'F', 'L', 'F', 'F', 'R', 'L', 'F', 'L', 'F'], ['R', 'R', 'L', 'R', 'F', 'R', 'L', 'L', 'R', 'F', 'L'], ['R', 'L', 'L', 'R', 'R', 'F', 'R', 'L', 'R', 'L', 'R'], ['R', 'F', 'F', 'F', 'L', 'F', 'L', 'F', 'L', 'R', 'R'], ['R', 'L', 'L', 'R', 'R', 'F', 'R', 'L', 'F', 'L', 'F']]
# print(z)
# print()
# y= mutate(z,.9)
# print("wjole s")
# print(y)

