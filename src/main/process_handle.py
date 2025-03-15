#process manaer/orchestrator
#point to constructors
from .constructor.introduction_process import introduction_process
from .constructor.people_finder_constructor import people_finder_constructor
from .constructor.people_register_constructor import people_register_constructor

def start():
    while True:
        command = introduction_process()
        if command == '1':
            people_register_constructor()
        elif command == '2':
            people_finder_constructor()
        elif command == '0':
            exit()
        else:
            print('\nInvalid command!!\n\n')

