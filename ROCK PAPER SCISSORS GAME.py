#!/usr/bin/env python
# coding: utf-8

# In[4]:


count_h = 0
count_c = 0
print("___________Rock...Paper...Scissors___________\n")
print("Hey! Welcome to the game. Lets begin...\n")
keep_playing = True
while keep_playing:
    import random
    
    c_choice = random.choice(['rock', 'paper', 'scissors'])
    print('The computer chooses ' + c_choice)
    h_choice = random.choice(['rock', 'paper', 'scissors'])
    print('Human chooses ' + h_choice)
    
    if((h_choice=='rock' and c_choice=='scissors') or (h_choice=='scissors' and c_choice=='paper') or 
      (h_choice=='paper' and c_choice=='rock')):
        print("Human wins")
        count_h+=1
    elif(h_choice==c_choice):
        print("Draw")
    else:
        print("Computer wins")
        count_c+=1
        
    print("\nDo you want to play again?")
    answer = input()
    if answer=="no":
        keep_playing = False
        print("\nThanks for playing")
        print("Computer score: "+str(count_c))
        print("Human score: "+str(count_h))
        
        print("\nOverall results:")
        if count_c & count_h:
            print("Well played!\n")
        elif count_c == count_h:
            print("It's a draw")
        else:
            print("You win!!!")
        print("___________Rock...Paper...Scissors___________")

