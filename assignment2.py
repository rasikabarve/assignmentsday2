# -*- coding: utf-8 -*-
"""assignment2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15wwNblwCPe5qK66-CSrh72LpIJhzf1Ik
"""

input=4600
if  input <= 1000:
  print("safe to land") 
elif input > 1000 and input<=5000:  
  print("bring down") 
else:
    print("turn aound")

lower= 1
upper= 200
print("prime no between", lower ,"and", upper,"are:")
for num in range(lower,upper+1):
  if num>1:
    for i in range (2,num):
      if(num%i)==0:
         break
      else:
        print(num)
        break