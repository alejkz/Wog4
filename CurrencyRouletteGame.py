#Method #1: gets currency and generates interval.
def get_money_interval(difficulty,num):
    import requests
    import random

    #Generate random number
    random_num = random.randrange(1, 100)
    #API request to exchange rate
    url = 'https://v6.exchangerate-api.com/v6/dcf5d4e64604e454a71cba24/pair/ILS/USD'
    response = requests.get(url)
    data = response.json()
    conversion = float(data['conversion_rate'])
    #Creating total
    total = random_num * conversion
    print(total)

    if num == total or (num < total and num > (total - ( 5 - difficulty))) or (num > total and num < (total + (5 - difficulty))):
     print("You're in the safe range")
    else:
        print("Fuck off you failure")
#Method #2: Gets an input from the user
def get_guess_from_user():
    num = int(input("Guess the number of USD generated randomly:\n"))
    return num
#Method #3
def play(d):

    n = get_guess_from_user()
    get_money_interval(d, n)

                                                      #Method #1: gets currency and generates interval.
def get_money_interval(difficulty,num):
    import requests
    import random

    #Generate random number
    random_num = random.randrange(1, 100)
    #API request to exchange rate
    url = 'https://v6.exchangerate-api.com/v6/dcf5d4e64604e454a71cba24/pair/ILS/USD'
    response = requests.get(url)
    data = response.json()
    conversion = float(data['conversion_rate'])
    #Creating total
    total = random_num * conversion
    print(total)

    if num == total or (num < total and num > (total - ( 5 - difficulty))) or (num > total and num < (total + (5 - difficulty))):
     print("You're in the safe range")
    else:
        print("Fuck off you failure")
#Method #2: Gets an input from the user
def get_guess_from_user():
    num = int(input("Guess the number of USD generated randomly:\n"))
    return num
#Method #3
def play(d):

    n = get_guess_from_user()
    get_money_interval(d, n)

