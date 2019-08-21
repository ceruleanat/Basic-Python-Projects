#
# Python:   3.7
#
# Author:   Natalie Farrell
#
# Purpose:  Learning from The Tech Academy.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable to
#           back to the calling function.





def start():
    print("Hello, {}!".format(get_name()))



def get_name():
    name = input("What is your name? ")
    return name









if __name__ == "__main__":
    start()
