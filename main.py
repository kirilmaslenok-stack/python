from random import choice
from unittest import case

collections = ['task''task1']
is_start = True

while(is_start):
    print("1 - позвать степашу | 2 - позвонить степаше")
    choice_user = input("(1 или 2)  ")
    match choice_user:
        case '1':
            print(collections)
        case '2':
            collections.append('task')
            print(collections)
        case _:
            print("какого пунка нету")
