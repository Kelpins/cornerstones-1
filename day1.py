"""

name = "Kellan"
major = "Electrical and Computer Engineering"
num_courses = 4
days_on_campus = ["Monday", "Tuesday", "Wednesday", "Friday"]


def arr_to_str(arr):
    result = ""
    for i in range(len(arr)):
        if i == len(arr) - 1:
            result += "and "
        result += arr[i]
        result += "s"
        if i < len(arr) - 1:
            result += ", "
    return result


print(
    "My name is "
    + name
    + ", my major is "
    + major
    + ", I am taking "
    + str(num_courses)
    + " courses this semester, and I am on campus on "
    + arr_to_str(days_on_campus)
    + "."
)

-------------------------------------------------

1- Write a program that asks the user to input a length in foot and calculate the same length in inches.
note: inch= 12*foot. Print out a statement that includes the original input and the modified value,

e.g. The value of 24 inches is equivalent to 2 feet.

If you are interested extend the program to change the user input to meter.


# asks the user for a length to convert from feet to inches
length = input("What length would you like to convert to inches? ")

# ensures length input is a valid number
try:
    length = float(length)
except:
    print("please input a valid number")
    exit()

# converts to inches and prints the result
inches = 12 * length
print("Your inches value is: " + str(inches))

-------------------------------------------------

2- write a program in python that asks an instructor how many classes they have
and how many students in each class they have (the number of students in all classes is similar).
Then calculate the total number of students they have and print it out as: the total number of students you have is


num_classes = int(input("How many classes do you have? "))
num_students = int(input("How many students do you have in each class? "))
total_students = num_classes * num_students
print("The total number of students you have is " + str(total_students))

--------------------------------------------------

3- In an experiment we want to measured the velocity of water at a certain point near the wall in a pipe.
the experiment should take 2 hours. Ask the user how long they want to be the interval between two
consecutive measurement in second. Calculate how many data elements (velocity measured) we have.
print out the number of data as: the number of data for this test will be ... .
try different values for time interval and check the output for each of them.
Question: the number of data should be an integer, we can have 14 data elements but not 14.3 data element,
how do you do this calculation?

Example: I want the interval between the two measurement be 6 seconds so the number of data elements
collected in 2 hours is: 2*3600/6=1200


interval_length = int(input("What is the interval length in seconds? "))
total_time = 2 * 3600  # total time in seconds
num_data = (
    total_time // interval_length
)  # integer division to get whole number of data points
print("The number of data for this test will be " + str(num_data))


-------------------------------------------------------

4- write a program that ask the user for two different numbers and assign them to two different variables,
then swap the values.


#user inputs two numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

#prints the original values
print("The first number is: " + str(num1))
print("The second number is: " + str(num2))

#set a temporary variable to hold one of the values during the swap
temp = num1

#swaps the values
num1 = num2
num2 = temp

#prints the swapped values
print("The first number is now: " + str(num1))
print("The second number is now: " + str(num2))

"""
