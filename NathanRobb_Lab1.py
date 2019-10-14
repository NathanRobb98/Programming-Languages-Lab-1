#Idris's Lab / coursework template
 
#Nathan Robb, NR36, H00248421        <--- so we know who you are 
#F28LL Lab / Coursework PY1                         <--- sanity check


#You may assume variables, procedures, and functions defined in earlier questions 
#in your answers to later questions, though you should add comments in code explaining 
#this if any clarification might help read your code.

#$ The file extension of this template is .txt.  It should be .py, but this does not play nice with TurnItIn.



################################################################################
#Question 1   <--- Yes, so we know what question you think you're answering 
print()
print('Question 1')
print()

#creating the variables
course = "python" 
rating = 219

#printing the variables individually 
print(course)
print(rating)
#printing the variables together - as rating is an int, it must be changed to string to print with course
print(course + " " + str(rating))



#END ANSWER TO Question 1
################################################################################


################################################################################
#Question 2   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 2')
print()

import math

b = 3
c = 4

a = math.sqrt((b*b) + (c*c)) #calculating the hypotenuse and assigning it to variable a

print(a)



#END ANSWER TO Question 2
################################################################################


################################################################################
#Question 3   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 3')
print()

print(type(a))
print(type(b))
print(type(c))

#a is not saved as an int, as it's value has been calculated.  




#END ANSWER TO Question 3
################################################################################


################################################################################
#Question 4   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 4')
print()

a = int(a) #converting the float type to an integer 
print(type(a)) #proving that the change has been successfull 

#Q4.c) print a + " squared equals " + b + " squared " + c + " squared."
#Q4.d) You can't concatenate strings and integers in python - integers must be converted to Strings
#cont.. in python 3, brackets are also required in order to print a statement.

#printing the statement from Q4.c) correctly
print(str(a) + " squared equals " + str(b) + " squared + " + str(c) + " squared.")



#END ANSWER TO Question 4
################################################################################


################################################################################
#Question 5   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 5')
print()

def largest(intlist):
    maxvalue = intlist[0] #setting the first value of the list to the max value variable initially 
    for x in intlist: #looping through the lsit
        if x > maxvalue: #if the current value is larger than the curent maxvalue
            maxvalue = x #then the current list value becomes the new maxvalue
    return maxvalue

#The lists that the above function is going to loop trough to find the max value   
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([5,4,3,3,2,1]))
print (largest([1,2,3,4,5,6,7,8,9,10]))
print (largest([1,1,1,1,1,1,1]))
print (largest([1.0,2.0,3.0,4.0,5.0,6.0]))
print (largest(['a','s','d','f','g','h','i','j','k','l']))



#END ANSWER TO Question 5
################################################################################


################################################################################
#Question 6   <--- Yes, so we know what question you think you're answering 
print()
print()
print('Question 6')
print()

####
print("Displaying the multiplication table as shown in the lab exercises document")
print()
####

#displaying the first line/row (the multipliers)
print(end = "\t") #tab
for line in range(1,10): #print values 1 to 10, tab after each value printed
    print(line,end = "\t")
print(end="\n") #taking a new line so that the numbers display correctly when the screen is made larger

#nested loop to display the remainder of the multiplication table
x = 1
for multiplum in range(1,10):
    print(multiplum, end="\t") #printing the first column
    for number in range(x): # looping so that the number of columns printed increment in 1
        print(multiplum * (number+1), end="\t") #printing the next 9 columns
    x = x + 1 #adding 1 to x, to increment the number of columns printed
    print(end="\n")


####
print()
print("Displaying a full multiplication table")
print()
####

#displaying the first line/row (the multipliers)
print(end = "\t") #tab
for line in range(1,10): #print values 1 to 10, tab after each value printed
    print(line,end = "\t")
print(end="\n") #taking a new line so that the numbers display correctly when the screen is made larger

#nested loop to display the remainder of the multiplication table
for multiplum in range(1,10):
    print(multiplum, end="\t") #printing the first column(the multipliers)
    for number in range(1,10): 
        print(multiplum * (number), end="\t") #printing the next 9 columns
    print(end="\n")


#END ANSWER TO Question 6
################################################################################
