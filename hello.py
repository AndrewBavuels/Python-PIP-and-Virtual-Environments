import random

def choose_options():
    options = ('rock', 'paper', 'scissors')
    user_option = input('rock, paper, or scissors => ')
    user_option = user_option.lower()

    if user_option not in options:
        print('That option is not valid')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Tie!')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('Rock beats scissors')
            print('User wins!')
            user_wins += 1
        else:
            print('Paper beats rock')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('Paper beats rock')
            print('User wins!')
            user_wins += 1
        else:
            print('Scissors beats paper')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('Scissors beats paper')
            print('User wins!')
            user_wins += 1
        else:
            print('Rock beats scissors')
            print('Computer wins!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0  
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('Computer wins:', computer_wins)
        print('User wins:', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None:
            continue
        
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('The winner is the computer')
            break

        if user_wins == 2:
            print('The winner is the user')
            break

run_game()
