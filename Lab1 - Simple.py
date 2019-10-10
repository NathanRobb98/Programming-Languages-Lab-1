#Question 1
print("Question 1")

course = "python"
rating = 219

print(course + " " + str(rating))



#Question 2
print("Question 2")

import math

b = 3
c = 4

a = math.sqrt((b*b) + (c*c))

print(a)



#Question 3
print("Question 3")

print(type(a))
print(type(b))
print(type(c))



#Question 4
print("Question 4")

a = int(a)
print(type(a))

#print (a + " squared equals " + b + " squared " + c + " squared." )
#You can't concatenate strings and integers in python - integers must be changed to String
print(str(a) + " squared equals " + str(b) + " squared " + str(c) + " squared.")



#Question 5
print("Question 5")

def largest(intlist):
    maxvalue = intlist[0]
    for x in intlist:
        if x > maxvalue:
            maxvalue = x
    return maxvalue

#Test   
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([1,2,3,4,5,6,7,8,9,0]))
print (largest([5,4,3,3,2,1]))
print (largest([1,2,3,4,5,6,7,8,9,10]))
print (largest([1,1,1,1,1,1,1]))
print (largest([1.0,2.0,3.0,4.0,5.0,6.0]))
print (largest(['a','s','d','f','g','h','i','j','k','l']))



#Question 6
print("Question 6")

#for line in range(1,10):
 #   for table in range (1,10):
  #      print(line * table, "\t")
    #print


# The heading
print(end = "\t")
for line in range(1,10):
    print(line,end = "\t")
print(end="\n")

# The double for-loop
x = 1
for multiplum in range(1,10):
    print(multiplum, end="\t") # First column
    for number in range(x):
        print(multiplum * (number+1), end="\t") # Next 9 columns
    x = x + 1
    print(end="\n")





