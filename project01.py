name = input("Hey! Type your Name: ")
print("Hello " + name + " Wlecome to my game!")

should_we_play = input("Do you want to play? (yes/no)").lower()
if should_we_play == "yes" or should_we_play == "y":
    print("We are goona Play!")
    weapon = input("Chose a weapon (sword/axe): ").lower()

    direction = input("Do you want to go left or right? (left/right)").lower()
    if direction == 'left' or direction == "l":
        print("Okay we went left! and Game Over")
    elif direction == 'right' or direction == 'r':
        choice = input("Okay, now you see a Bridge, Do you want to swim under it or crosss is?: (swim/cross)").lower()
        if choice == "swim" and weapon == "axe":
            print("You continue")
        elif choice == "cross" or choice =="sword":
            print("You found a door, Game ends.")
        elif choice == "cross" or choice== "axe":
            print("you found a cliff, The game ends Here ;>")
        else:
            print("Game Over! :)")
    else: 
        print('Not a valid input: ')

else:
    print("We are not playing ;>")