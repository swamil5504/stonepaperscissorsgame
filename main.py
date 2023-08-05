##Game is between Computer and the Player##

import random #module for generating random numbers#

def game(comp,you): #function containing all the possible outcomes (r-ROCK,p-PAPER,s-SCISSOR)#
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print("Computer's Turn: Rock(r),Paper(p),Scissor(s)\n.....DONE....")
randNo = random.randint(1,3) #built-in function of *random* module for generating numbers between the range specified by the user#

#Converting the randomly generated integers to r,p,s#
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo ==3:
    comp = 's'


you = input("Its Your Turn Now:- Rock(r),Paper(p),Scissor(s)?\n")
a = game(comp,you) #Calling the fucntion on line 5#

print(f"Computer chose--{comp}") #Used fstring here, that makes printing the variables more easy#
print(f"You chose--{you}")       #-//-#

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!!!")
else:
    print("You lose XD")


