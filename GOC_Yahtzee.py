#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product

#Attempted to simulate a random result from the roll of a dice, 
#However, was unable to handle appropriately while using the for loops below 

##To Generate random but unique number from 1 to 6
#import random
#mylist1=random.sample(l,6)

#Please Input the values of the 3 Dice at the bottom section of the code in list x

def GOC_Yahtzee(x):

    l=[1,2,3,4,5,6]    
    Exp=[]
    Roll=[]    
    currentSum=x[0]+x[1]+x[2]
    
    #if all 3 are the same then do not roll
    if((x[0]==x[1]) and (x[1]==x[2])):
        print("All 3 Dice have the same value. You won!!!")
        return
    
    #For rolling 1 dice: 1st, 2nd or 3rd dice
    #The code pops the dice values one by one and calculates expectation values using the remaining 2 values in list x
    #The expectation and roll values are appended to an array to keep track
    
    for i in range(0,3):
        sum1=0
        CNValue1=0
        Totalsum1=0
        
        x1 = list(x)
        x1.pop(i)
        
        for j in range(1,7):
            if(j==x1[0] and j==x1[1]):               #Yahtzee!
                sum1=25
                CNValue1 = float((1/6)*sum1)        #probability of getting any number is 1/6
                Totalsum1 = Totalsum1 + CNValue1
            else:
                sum1 = x1[0] + x1[1] + j
                CNValue1 = float((1/6)*sum1)
                Totalsum1 = Totalsum1 + CNValue1
        Roll.append([i+1])    
        Exp.append(Totalsum1)
    
    #For rolling 2 dice: (1,2) or (2,3) or (1,3)
    #The code pops the dice value and calculates expectation values using the popped value stored in a variable
    #The expectation and roll values are appended to an array to keep track

    for i in range(0,3):
        sum2=0
        CNValue2=0
        Totalsum2=0
        
        x2 = list(x)
        x3 = x2.pop(i)
        [a,b]=x2    
        
        for j in range(1,7):
            for k in range(1,7):
                if(j==k and k==x3):                 #Yahtzee!
                    sum2 = 25
                    CNValue2 = float(1/36)*sum2     #probability of getting any 2 numbers is 1/36
                    Totalsum2 = Totalsum2 + CNValue2
                else:
                    sum2 = j + k + x3
                    CNValue2 = float(1/36)*sum2
                    Totalsum2 = Totalsum2 + CNValue2
        
        ind = x.index(a)
        ind2 = x.index(b,ind+1)    
        Roll.append([ind+1,ind2+1])
        Exp.append(Totalsum2)
   
    #For rolling 3 dice
    #The code creates list of all possible values from roll of 3 dice, sums the tuple and calculates expectation
    #The expectation and roll values are appended to an array to keep track

    a=list(product(l,repeat=3))
    #print(a)
    sumlist = sum([sum(z) for z in a])
    sumlist = sumlist + 6*25 - 3*(sum(range(1,7))) #for adjusting values when we hit Yahtzee - (1,1,1), (2,2,2) etc.
    Exp3=float((1/216)*sumlist)                    #probability of getting any 3 numbers is 1/216
    Exp.append(Exp3)
    Roll.append([1,2,3])
        
    maxExp = max(Exp)
    
    if(maxExp<currentSum):
        print("Do not roll any dice!")
    else:
        index_=Exp.index(max(Exp))
        
        FinalRoll = Roll[index_]
        print("Roll dice:", FinalRoll)

#Please input the values of the 3 Dice here:
#1st value: 1st Dice, 2nd value:2nd Dice, 3rd value: 3rd Dice
        
x=[1,2,6]
GOC_Yahtzee(x)