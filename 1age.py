import datetime
import time

name = input("Enter you Name Please: ")
age = int(input("please enter your age: "))

cyear, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')

print("Curent Year is: " + cyear)

anniv = (100 - age)

tobean = int(cyear) + int(anniv)

#print("Hello " + str(name) + ", In the year " + int(tobean) + "You will complete your hundred years")
print( "Dear ", name + " You will complete you age 100 in the year of: ", + int(tobean))



            