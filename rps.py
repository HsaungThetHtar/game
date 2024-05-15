import random
while True:
    print('Winning rules of the game Rock Paper Scissors are:\n'
              + "Rock vs Paper -> Paper wins \n"
              + "Rock vs Scissors -> Rock wins \n"
              + "Paper vs Scissors ->  Scissors wins \n")
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        choice = input('Enter your choice between 1 to 3:')
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print('Enter a number:')

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please !!!'))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is ',choice_name)
    print("Now it is Computer's Turn")

    com_choice = random.randint(1,3)

    while com_choice == choice:
        com_choice = random.randint(1,3)
    if com_choice == 1:
        com_choice_name = 'Rock'
    elif com_choice == 2:
        com_choice_name = 'Paper'
    else:
        com_choice_name = 'Scissors'
    print('Computer choice is ',com_choice_name)
    if choice == com_choice:
        print('It is a Draw')
    if (choice == 1 and com_choice == 2):
        print(f'Computer wins with {com_choice_name}!')
    elif (choice == 2 and com_choice == 1):
        print(f'You win with {choice_name}')
    if (choice == 1 and com_choice == 3):
        print(f'You win with {choice_name}')
    elif (choice == 3 and com_choice == 1):
        print(f'Computer wins with {com_choice_name}!')
    if (choice == 2 and com_choice == 3):
        print(f'Computer wins with {com_choice_name}!')
    elif (choice == 3 and com_choice == 2):
        print(f'You win with {choice_name}')

    ans = input('Do you want to play again? Y/N  ')
    ans = ans.lower()
    if ans != 'y':
        break
print('Thank u for playing!')


