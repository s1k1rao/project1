
# coding: utf-8

# #date:13TH OCT 2018
# #DISCRIPTION:SPACE ADVENTURE GAME

# In[2]:


import random 
import time
check2=True
while check2==True:    
    name=input("enter your name")
    print("hey",name,"welcome to the inter galaxy headquarters")
    time.sleep(2)
    print("we are facing a serious trouble due to alien invation,would you like to be the one to save our galaxy from this big problem?")
    check3=True
    while check3==True:
        choice1=input("enter yes of no")
        if choice1=="yes":
            check3=False
            print("good,first you need to choose a weapon to defend yourself in their world")
            time.sleep(2)
            check=True
            while check==True: 
                weapon=input("choose a weaopon")
                if weapon=="mavrick" or "ak47":
                    check=False
                    print("wow",weapon,"is a really good weapon,wish you all the best,")
                    time.sleep(2)
                    print("................entering the enemy grounds.............")
                    time.sleep(4)
                    print("YOU ARE NOW IN THE ENEMY AREA")
                    time.sleep(4)
                    print("INTENSE BATTLE GOING ON BETWEEN YOU AND YOUR ENEMY")
                    time.sleep(4)
                    print("CONGO,YOU HAVE WON THE BATTLE AGAINST THE ALIEN ENEMIES AND YOU HAVE SUCCESFULLY SAVED YOUR GALAXY ")
                    print("BUT WHILE YOU WERE BATTELING AGAINST THE ALIENS YOU LOST YOUR MAP AND ARE LOST IN THE BASE")
                else:
                    check=True
            print("NOW YOU HAVE TO CHOOSE BETWEEN THE TWO PATHS")
            choice2=int(input("enter either 1 or 2"))
            n=random.randint(1,choice2) 
            if n==1:
                print("hurray you have chosen the right path and you have reached home safely and your havhe been rewarded handsomely for your bravery")
                choice3=input("do you want to play again?.type yes or no")
                if choice3=="yes":
                    check2=True
                else:
                    check2=False
            else:
                print("sorry you were chicken fried in the gamma ray burst")
                choice3=input("do you want to play again?.type yes or no")
                if choice3=="yes":
                    check2=True
                else:
                    check2=False
        else:
            check3=True

