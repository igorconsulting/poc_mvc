#process manaer/orchestrator
#point to constructors
from .constructor.introduction_process import introduction_process

def start():
    while True:
        command = introduction_process()
        if command == '1':
            print('You have selected 1')
        elif command == '2':
            print('You have selected 2')
        elif command == '0':
            exit()
        else:
            print('\nInvalid command!!\n\n')

