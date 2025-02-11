"""
This module contains example greeting functions
"""

# create a function
def say_hello():
    """
    Says hello to all persons
    """
    print("Hello Everyone!")
def say_hello_to_someone(name):
    """
    Says hello to a specific individual (name: str)
    """
    return "Hello " + name


def main():
    # use / call the function
    print("My name is " + __name__)
    say_hello()
    print(say_hello_to_someone('Bob'))
    message = say_hello_to_someone("Julie Dooley")
    print(message)
    print(message.upper())

#the main trick
if __name__ == "__main__":
    main()
