__author__ = 'Alex'


def boop( my_value ):  # Has spaces around both.
	print my_value  # Has a tab


def beep():
	value = "Hello"  # Has a tab
	boop(value )  # Space only on the end. Has a tab

if __name__ == "__main__":
	beep( )  # Spaces between empty braces. Has a tab
