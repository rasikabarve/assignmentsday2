# -*- coding: utf-8 -*-
"""assignment no.1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dM08AfB21xy_ourZ6HVohFG2Yufw7dnR
"""

#list and its default function
#1 adding element as a value of list

list= ['rasika','barve','electronics',1997]
  list.append(2019)
  print(list)

#2 insert and element at particular position

list= ['rasika','barve','electronics',1997]
  list.insert(3,2020)
  print(list)

#3add content of list 1 ino list 2

list1 = [2,8,6,9]
  list2 = [1,2,3,4,5]
  list1.extend(list2)
  print(list1)

#4 sum of all element in the list
list =[121,144,169,169,225] 
print(sum(list))

#5 clculate total occurance of element in the list
list=[1,2,5,8,7,4,6,2,8,7,2]
print(list.count(2))

# dictionary and its defalut functions
#1 print a dictionary
thedict={
    "war": "panipat battle 3rd", 
    "between": " maratha empire vs afghan army",
    "year":"1761"
}
print(thedict)



#2 accesing item
thedict={
    "war": "panipat battle 3rd", 
    "between": " maratha empire vs afghan army",
    "year":"1761"
}
x = thedict["year"]
print(x)



#3 change value
thedict={
    "war": "panipat battle 3rd", 
    "between": " maratha empire vs afghan army",
    "year":"1761"
}
thedict["year"] = 1762
print(thedict)



#4 loop through dictionary
thedict={
    "war": "panipat battle 3rd", 
    "between": " maratha empire vs afghan army",
    "year":"1761"
}
for x in thedict:
  print(x)

#5 print all the values of the dictionary
thedict={
    "war": "panipat battle 3rd", 
    "between": " maratha empire vs afghan army",
    "year":"1761"
}
for x, y in thedict.items():
  print(x, y)

# sets and its default function
#1 add element to the sets
grocery = { "sugar","suji","jaggry"} 
grocery.add("moong dal")
print(grocery)

#2 clear the sets
grocery = { "sugar","suji","jaggry"} 
grocery.clear()
print(grocery)

#3 remove element from set
grocery = { "sugar","suji","jaggry"} 
grocery.remove("sugar")
print(grocery)

#4 pop the element
grocery = { "sugar","suji","jaggry"} 
grocery.pop()
print(grocery)

#5 set union
grocery1 = { "sugar","suji","jaggry"} 
grocery2 = {"apple","banana", "grapes"}

grocery= grocery1.union(grocery2)
print(grocery)

#tuples and its default function
#1 create tuple
thistuple ={"sugar","suji","jaggry"}
print(thistuple)

#2 accessing tuple item
thistuple = {"sugar","suji","jaggry"}

print(thistuple[1])

#3 count of element
thistuple={'a','e','i','i','o','u','i'}
thistuple.count(i)
print(i)

#stringg and default method
#1capitalise string
string="python upgrade"
capitalize_string= string.capitalize()
print('capitalize string:', capitalize_string)

#2 count the number of occerance in the givn substring
string=" python is awsome,isn,t it"
substring= "is"
count=string.count(substring)
print(count)

#3 lower case string
string="PYTHON UPGRADE"

print("lower case string:", string.casefold())

#4 center()method with fillchar
string=" python is awsome"
new_string= string.center(24)
print("center string:", new_string)

#5 basic formatting
print("the number is:{:d}".format(123))
print("the number is:{:f}".format(123.654))