# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:01:35 2022

@author: Gunjan
"""

#jumbled GAME

import random 

def choose():
    words=['rainbow','computers','science','programming','mathematics','player','conditions','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,pp1,pp2):
    print(p1n," your score is :",pp1)
    print(p2n,'your score is :',pp2)
    print('thank you for playing ')
    print('have a nice day ')
    
def play():
    p1name=input("player 1 , please enter your name")
    p2name=input("player 2, please enter your name")
    pp1=0
    pp2=00
    turn = 0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if turn%2==0:
            print(p1name,'Your turn ')
            ans=input('What is on my mind? ')
            if ans==picked_word:
                pp1=pp1+1
                print('Your score is : ',pp1)
                
            else:
                print('better luck next time, I throught: ',picked_word)
            c=int(input("press 1 to continue or 0 to end "))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
            
            
         #player 2
        else:
             print(p2name,'Your turn ')
             ans=input('What is on my mind? ')
             if ans==picked_word:
                 pp2=pp2+1
                 print('Your score is : ',pp2)
                 
             else:
                 print('better luck next time, I throught: ',picked_word)
             c=int(input("press 1 to continue or 0 to end "))
             if(c==0):
                 thank(p1name,p2name,pp1,pp2)
                 break    
        turn=turn+1
        
    
    
play()