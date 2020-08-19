from random import randint

while True:
    print("enter your choice ----> rock , paper or scissors ")
    choice = input()
    choice = choice.lower()
    print("My choice is -> ", choice)

    choices = ['rock', 'paper', 'scissors']
    computer_choice = choices[randint(0, 2)]
    print("computer_choice is ----> ", computer_choice)
    if choice in choices:
        if choice == 'rock':
            if computer_choice == 'rock':
                print("it is a tie")
            elif computer_choice == 'paper':
                print("you loose")
            elif computer_choice == 'scissors':
                print("you win")

        if choice == 'paper':
            if computer_choice == 'rock':
                print("you win")
            elif computer_choice == 'paper':
                print("it's a tie")
            elif computer_choice == 'scissors':
                print("you loose")

        if choice == 'scissors':
            if computer_choice == 'rock':
                print("you win")
            elif computer_choice == 'paper':
                print("you loose")
            elif computer_choice == 'scissors':
                print("it's a tie")

    else:
        print(" !!!!!!!!!!!  invalid input, please select between rock,paper or scissors  !!!!!!!!")

        print()
