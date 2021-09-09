from Live import load_game, welcome

welcome("Alex")
load_game()# Generates random list N sized.
def generate_sequence(difficulty):
    import random
    res = [random.randrange(1,100,1) for i in range(int(difficulty))]
    return res
#Gets a list from user - N sized.
def get_list_from_user(difficulty):
    user_lst = []
    for i in range(difficulty):
        num = int(input("Enter a number:\n"))
        user_lst.append(num)
    return user_lst
#Cheks if lists are equal
def is_list_equal(lst1,lst2,difficulty):

    if lst1 == lst2:
        print("True")
    else:
        print("False")
#General function
def play(N):
    import time
    import os


    print("Were starting in 5 seconds,get ready, the numbers are quick!\n")
    time.sleep(5)
    random_lst = generate_sequence(N)
    for i in range(N):
        print(random_lst[i])
        time.sleep(0.7)
        os.system('cls')

    print("Now its your turn to guess the numbers by their order, good luck!\n")
    user_lst = get_list_from_user(N)
    final = is_list_equal(random_lst,user_lst,N)




