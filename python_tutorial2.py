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
    f_name = "Robert"
    l_name = "Fink"
    age = 30
    gender = "Male"
    get_info(f_name,l_name,age,gender)



def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name,l_name,age,gender))









if __name__ == "__main__":
    start()
