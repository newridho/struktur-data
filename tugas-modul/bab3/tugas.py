#Ubah Program !!
#Dari Batu, Kertas, Gunting menjadi Semut, Gaja, Orang 
import random
import os
import re

def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')

            if response.lower() not in valid_responses:
                raise ValueError('Invalid response. Please enter "Yes" or "No"')
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        except ValueError as err:
            print(err)

def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Semut, Orang, Gajah!')

        user_choice = input('Choose your weapon [S]emut], [O]rang, or [G]ajah: ') 

        if not re.match("[SsOoGg]", user_choice):
            print('Please choose a letter:')
            print('[S]emut], [O]rang, or [G]ajah')
            continue

        print('You chose: ' + user_choice)

        choices = ['S', 'O', 'G']
        opp_choice = random.choice(choices)

        print(f'I chose: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('Tie!')
            play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'G':
            print('Semut mengalahkan Gajah, saya menang!')
            play = check_play_status()
        elif opp_choice == 'G' and user_choice.upper() == 'O':
            print('Gajah mengalahkan Orang! Saya menang!')
            play = check_play_status()
        elif opp_choice == 'O' and user_choice.upper() == 'S':
            print('Orang mengalahkan Semut, saya menang!')
            play = check_play_status()
        else:
            print('Kamu menang!')
            play = check_play_status()

if __name__ == '__main__':
    play_rps()
