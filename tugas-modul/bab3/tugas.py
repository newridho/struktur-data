#Ubah Program !!
#Dari Batu, Kertas, Gunting menjadi Semut, Gaja, Orang 
import random
import os
import re

def cekStatus():
    pilih = ['y', 't']
    while True:
        try:
            response = input('Mo main lagi? (y or t): ')

            if response.lower() not in pilih:
                raise ValueError('Pilihan Tidak Valid. Pilih "y" atau "t"')
            if response.lower() == 'y':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
        except ValueError as err:
            print(err)

def main():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Semut, Orang, Gajah!')

        user_choice = input('Pilih [S]emut], [O]rang, or [G]ajah: ') 

        if not re.match("[SsOoGg]", user_choice):
            print('Pilih donk:')
            print('[S]emut], [O]rang, or [G]ajah')
            continue

        print('Pilihanmu: ' + user_choice)

        choices = ['S', 'O', 'G']
        opp_choice = random.choice(choices)

        print(f'Aku milih: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('Imbang!')
            play = cekStatus()
        elif opp_choice == 'S' and user_choice.upper() == 'G':
            print('Semut mengalahkan Gajah, saya menang!')
            play = cekStatus()
        elif opp_choice == 'G' and user_choice.upper() == 'O':
            print('Gajah mengalahkan Orang! Saya menang!')
            play = cekStatus()
        elif opp_choice == 'O' and user_choice.upper() == 'S':
            print('Orang mengalahkan Semut, saya menang!')
            play = cekStatus()
        else:
            print('Kamu menang!')
            play = cekStatus()

if __name__ == '__main__':
    main()
