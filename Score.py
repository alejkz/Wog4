def add_score(diff):

    pow = (diff * 3 ) + 5
    try:
        with open("/Users/alex/Desktop/Score.txt", 'r') as g:
            data = g.readlines()
            print("Current score is: ",pow)
    except FileNotFoundError:
        print("File doesn't exist")
        with open("/Users/alex/Desktop/Score.txt", 'w') as g:
            g.write(str(pow))

x = int(input("Number input\n"))
add_score(x)
