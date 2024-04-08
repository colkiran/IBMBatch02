
class TooTiny(Exception):
    pass

class TooSmall(Exception):
    pass

class TooLarge(Exception):
    pass

age = 105

try:
    if age < 7:
        raise TooTiny
    elif age < 18:
        raise TooSmall
    elif age > 100:
        raise TooLarge
    else:
        print("You can cast your valuable vote.....")
except TooTiny:
    print("Too very tiny to cast the vote.....")
except TooSmall:
    print("Too small to cast the vote.....")
except TooLarge:
    print("Too Old to cast the vote.......")