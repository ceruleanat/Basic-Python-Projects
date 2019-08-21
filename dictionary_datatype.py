Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary['index2']
2
>>> dic_users = {'em_1234': {'fname': 'Robert', 'lname': 'Fink', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Nat', 'lname': 'Farrell', 'phone': '760-300-5074'} }
>>> print(dic_users['em_1235'])
{'fname': 'Nat', 'lname': 'Farrell', 'phone': '760-300-5074'}
>>> print(dic_users['em_1235'] ['phone'])
760-300-5074
>>> print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1234']['phone']))
User: Nat Farrell
Phone: 123-456-7890
>>> >>> print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
SyntaxError: invalid syntax
>>> print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
User: Nat Farrell
Phone: 760-300-5074
>>> 
