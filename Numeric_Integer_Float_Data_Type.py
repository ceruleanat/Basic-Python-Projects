Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 1
>>> num2 = 2
>>> 
>>> 
>>> print(num1 + num2)
3
>>> num1 = 1.2
>>> num2 = 2.1
>>> print(num1 + num2)
3.3
>>> num1 = "1"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1) + num2)
3.1
>>> 
myList = [2,3,4]
>>> len(myList)
3
>>> for i in myList:
	print(i)

	
2
3
4
>>> myList[2]
4
>>> myList[0]
2
>>> myList.append(5)
>>> for i in myList:
	print(i)

	
2
3
4
5
>>> len(myList)
4
>>> print(myList)
[2, 3, 4, 5]
>>> 
