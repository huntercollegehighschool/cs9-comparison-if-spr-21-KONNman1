'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''


month = input("Enter the name of a month: ")

thirtyone = ["January", "january", "March", "march", "May", "may", "July", "july", 
             "August", "august", "October", "october", "December", "december"]
thirty = ["April", 'april', "June", "june", "September", "september", "Novemeber",  
          "november"]

if month in thirtyone:
  print("There are 31 days in this month.")

elif month in thirty:
  print("There are thirty days in this month.")

elif month == "February" or month == "february":
  print("There are 28 days in this month normally, and 29 days on leap years.")

else:
  print ("That is not a valid month.")