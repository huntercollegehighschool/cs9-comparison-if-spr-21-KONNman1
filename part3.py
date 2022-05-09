'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number: -2
Negative
Mot divisible by 3

Enter a number: 0
Zero
Divisible by 3

Enter a number:  5
Positive
Not divisible by 3
'''


#write your code below
number = int(input("Enter an integer: "))
divisible = number % 3

if number > 0:
  print ("Positive")
  if divisible == 0:
    print("Divisible by 3")
  if divisible != 0:
    print("Not divisible by 3")

if number < 0:
  print ("Negative")
  if divisible == 0:
    print("Divisible by 3")
  if divisible != 0:
    print("Not divisible by 3")

if number == 0:
  print("Zero")
  print("Divisible by 3")