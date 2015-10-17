# Modified by rules.tabs_spaces
# Modified by rules.brace_space
__author__ = 'Alex'


def boop(my_value):  # Has spaces around both.
    print my_value


def beep():
    value = "Hello"
    boop(value)  # Space only on the end.

if __name__ == "__main__":
    beep()  # Spaces between empty braces.
