# instructions
print("welcome to the treasure island ")
print("your mission is to find the treasure")
print("to be sucsessful in your game you have to choose the right paths")
print("it will totaly be based on your guess")
print("one wrong decision and the game will be over")

direction=input("where you wanna go 'left' or 'right'")
if direction =="left":
    print("you are save!! be carefull ahead to reach the winning point")
    choice2=input("you have reached to a river the island is in the middle"
          "If you want to swim type 'swim' or if you want to wait for a boat type 'wait' ")
    if choice2=="wait":
        choice3=input("you have reached to an island.there are three doors 'yellow' 'red' 'blue' where you want to go?")
        if choice3=="red":
            print("it is room full of fire.Game over")
        elif choice3=="yellow":
            print("you found treasure.you win")
        elif choice3=="blue":
            print("you enter the room full of beasts.Game over")
        else:
            print("you loose")            
else:
    print("sorry game over") 

