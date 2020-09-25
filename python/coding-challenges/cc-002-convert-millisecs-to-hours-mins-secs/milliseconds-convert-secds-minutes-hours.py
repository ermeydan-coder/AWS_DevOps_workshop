def convert(millis):
    # millis=input("Enter time in milliseconds: ")
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    return ("%d hour/s, %d minute/s, %d second/s" % (hours, minutes, seconds))

is_invalid = False

while True:
    info = """
###  This program converts Milliseconds into Hours, Minutes, and Seconds ###
(To exit the program, please type "exit")
Enter time in milliseconds  : """

    alphanum = input('\nNot Valid Input !!!\n'*is_invalid + info).strip()
    if not alphanum.isdecimal():
        if alphanum.lower() == 'exit':
            print('\nExiting the program... Good Bye')
            break
        else:
            is_invalid = True
            continue
    number = int(alphanum)
    if 0 < number < 1000:
        print(f'\nJust {alphanum} millisecond/s')
        is_invalid = False
    elif number>=1000:
        print(f'\n{convert(number)}')
        is_invalid = False
    else:
        is_invalid = True
