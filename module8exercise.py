# Module 8 exercise
import re

'''
# Given the following data:
str1 = "The answer is 42"
str2 = "What... is the air speed of an unladen swallow?"
str3 = "3.15; 2.383 and 11.039*2.77  1257.11"
str4 = "2020 / 08 / 14"
inList = [str1, str2, str3, str4]

# 1. Write regex to print the string if the string has:
# a. a digit
for myStr in inList: 
    if re.search("\d", myStr):
        print(myStr)
print()

# b. a number that's at least 3 digit long
for myStr in inList: 
    if re.search("\d{3}", myStr):
        print(myStr)
print()
# c. no letters
#if we loop for no of something which means zero if soemthing or any specific count of smething, we need to
#...add the anchors 
# The "^" anchor is always put at the beggining of the regex, and $ anchor is always at th end. 
#with both anchors in, we are describing what the entire line hsuld look like 
for myStr in inList: 
    if re.search("^[^a-z]+$", myStr, re.I): #one or more non-letters 
        print(myStr)
print()
for myStr in inList: 
    if re.search("^[^a-z]*$", myStr, re.I):#zero or more non-letters, wll allow for a blank line! 
        print(myStr)
print()
# 2. Write a regex to print 
# a. the 3 numbers of str4
#str4 = "2020 / 08 / 14"
myList = re.findall("\d+", str4)
for num in myList:
    print(num)
print()

m = re.search("(\d+) / (\d+) / (\d+)", str4)
print(m.group(1), m.group(2), m.group(3))

# b. the start location of the 3 numbers of str4
m = re.search("(\d+) / (\d+) / (\d+)", str4)
print(m.start(1), m.start(2), m.start(3))
print()


# 3. Write a regex to print:
# a. the first word of str2
print(re.search("\w+", str2).group()  )
print()

# b. the last word of str2

print(re.search("(\w+)\?$", str2).group(1)  )
print()


# c. both the first and last words of str2
#print(re.search("\w+", str2).group()  ) #cheap way but does search twice 
#print(re.search("(\w+)\?$", str2).group(1)  )

m = re.search("(\w+).* (\w+)\?$", str2)
print(m.group(1), m.group(2))
print()

# d. str2 with spaces changed to underscore
#str2 = "What... is the air speed of an unladen swallow?"
print(re.sub(" ", "_", str2)) #this subsitutes all spaces for underscore 
print()

# e. str2 with the ellipsis (...) removed
print(re.sub("\.\.\.", "" , str2)) #this subsitutes all spaces for underscore 
#the above code works because we only have one period in the line 
print()


# 4. Use regex to print only floating point numbers with 2 digits
# after the decimal point in str3
#str3 = "3.15; 2.383 and 11.039*2.77  1257.11"
print(re.findall("\d+\.\d{2}\\b", str3))#ad a comma after {2 so that you add the cases with 2 or more than 2! 

print()
'''


# Since this is the last exercise of the quarter, let's
# review as many topics as we can.

# 5. Write a loop that asks the user input for a birth date. 
# Keep asking until you get a valid birth date.

# Validate the user input with the following steps:
# a. check that the format of str4 is valid: yyyy-mm-dd
    
# b. check that the month is 1-12, day is valid for the 
# month (28, 30, or 31), and the year is between 1900 and 2100

# c. then print the date as mm/dd/yyyy
dayDict = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:31, 10:30, 11:31, 12:30 }
valid = False

while not valid :
    try: 
        userDate = input("Enter your birthdate: ")
        if not re.search("^\d{4}-\d{2}-\d{2}$", userDate):
            raise ValueError("Invalid input format")
        (year, month, day) = userDate.split("-")
        if not(1900 <= int(year) <= 2100):
            raise ValueError("Invalid year")
        if not(1 <= int(month) <= 12):
            raise ValueError("Invalid month")
        
        if not (1 <= int(day) <= dayDict[int(month)]):
            raise ValueError("Invalid day")
        print(month, '/',day,'/',year)
        valid == True
    except ValueError as e:
        print(e)
        
  