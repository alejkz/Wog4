def generate_number(difficulty):
    import random

    secret_number = random.randrange(0,difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    number = int(input("Guess what was the random number:\n"))
    return number

def compare_results(num1,num2):
    if num1 == num2:
        print("First number is equal to the second number !")
    else:
        print("Go fish")

def play(d):

    gen_num = generate_number(d)
    user_num = get_guess_from_user(d)
    compare_results(gen_num, user_num)

    again = input("Do you wish to play again?(Yes/No)")
    if again == "yes" or again == "Yes" or again == "YES" or again == "y":
        play(d)
    else:
        print("Thanks for participating")

                                                                                                                                                                                                                                        def generate_number(difficulty):
    import random

    secret_number = random.randrange(0,difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    number = int(input("Guess what was the random number:\n"))
    return number

def compare_results(num1,num2):
    if num1 == num2:
        print("First number is equal to the second number !")
    else:
        print("Go fish")

def play(d):

    gen_num = generate_number(d)
    user_num = get_guess_from_user(d)
    compare_results(gen_num, user_num)

    again = input("Do you wish to play again?(Yes/No)")
    if again == "yes" or again == "Yes" or again == "YES" or again == "y":
        play(d)
    else:
        print("Thanks for participating")

