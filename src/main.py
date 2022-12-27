import sys

def greetings():
    """
    Greets user and gets input.
    :return: input
    """
    print(f'Insert number of matches you would like to check:\n'
          f'(Press enter for default input, 10)\n'
          f'(Enter "q" to quit)')
    return input()


def check_input(user_input):
    """
    Checks if user input is allowed.
    False= not allowed; True= allowed.
    :return: exe
    """
    exe = False
    try:
        if('q'== user_input):
            #stop script
            exe = True
            print('Exit')


        elif(""==user_input):
            # default 10 games
            print(10)
            exe = True


        elif((1<=int(user_input)) and (50>=int(user_input))):
            print("Ok")
            exe = True

        else:
            print(f'>>> Input should be a number between 1 and 50\n')

    except:
        print(f'>>> Input should be a number\n')

    finally:
        return exe



def run():
    """
    Handles initialization and console arguments.
    :return: Stats
    """
    user_input=0

    while (False == user_input):
        num_matches = greetings()
        user_input = check_input(num_matches)
    print(f'end run()\n')
    sys.exit(0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()



