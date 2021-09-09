def welcome(player):
    print("Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"%(player))

def load_game():
    import MemoryGame
    import GuessGame
    import CurrencyRouletteGame

    game_choice = input("Please choose a game to play:\n1-Memory game - a sequence of numbers will appear for 1 second and you have to guess it back\n2-Guess Game - guess a number and see if you chose like the computer\n3-Currency Roulette - try and guess the value of a random amount of USD in ILS\n ")

    if game_choice == "1":
        difficulty_choice = int(input("Great! you've chosen the Memory game,now choose a difficulty from 1 to 5 (1 - Easiest , 5 - Hardest)\n"))
        print("Difficulty chosdef welcome(player):
    print("Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"%(player))

def load_game():
    import MemoryGame
    import GuessGame
    import CurrencyRouletteGame

    game_choice = input("Please choose a game to play:\n1-Memory game - a sequence of numbers will appear for 1 second and you have to guess it back\n2-Guess Game - guess a number and see if you chose like the computer\n3-Currency Roulette - try and guess the value of a random amount of USD in ILS\n ")

    if game_choice == "1":
        difficulty_choice = int(input("Great! you've chosen the Memory game,now choose a difficulty from 1 to 5 (1 - Easiest , 5 - Hardest)\n"))
        print("Difficulty chosen : %s"%(difficulty_choice))
        MemoryGame.play(difficulty_choice)

    elif game_choice == "2":
        difficulty_choice = int(input("Great! you've chosen the Guess game,now choose a difficulty from 1 to 5 (1 - Easiest , 5 - Hardest)\n"))
        print("Difficulty chosen : %s"%(difficulty_choice))
        GuessGame.play(difficulty_choice)

    elif game_choice == "3":
        difficulty_choice = int(input("Great! you've chosen Currency Roulette,now choose a difficulty from 1 to 5 (1 - Easiest , 5 - Hardest)\n"))
        print("Difficulty chosen : %s"%(difficulty_choice))
        CurrencyRouletteGame.play(difficulty_choice)

    else:
        print("Wrong input")

