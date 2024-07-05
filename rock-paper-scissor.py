rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
c1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("You chose")
if c1==0:
    print (rock)
if c1==1:
     print (paper)
if c1==2:
    print (scissors)
c2=random.randint(0,2)
print("Computer chose")
if c2==0:
    print (rock)
    if c1==2:
        print("You win")
    elif c1==1:
        print("You lose")
    elif c1==0:
        print("Draw")
if c2==1:    
    print (paper)
    if c1==2:
         print("You lose")
    elif c1==1:
         print("Draw")
    elif c1==0:
         print("You win")     
if c2==2:
    print (scissors)
    if c1==2:
         print("Draw")
    elif c1==1:
        print("You win")
    elif c1==0:
         print("You lose")
        
        
        
    