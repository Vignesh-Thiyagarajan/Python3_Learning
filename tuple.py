
str = ("Tall person",20,"perambur") #tuple1
print(str)

vasanth = tuple(["Short person",20,"Thinanur"]) #tuple2
print(vasanth)

if 20 in vasanth: #! using if condition and finding the value present in a tuple or not!!
    print ("yes")
else:
    print ("no")

Person_derails = vasanth[:] #! assigning tuple to a variable 
"""
Person_derails[0]="Noramal Person" #? in Tuple, elements inside the variable cannot be change
"""
print(Person_derails[0])

num_tuple = [1,2,3,4,5,6,7,8,9,10] #tuple3

for num in num_tuple: #iterate through tuple
    print(num)

random_letters = ('a', 'b', 'c', 'd', 'e', 'f','a') #tuple4 
# ? finding number of elements in the tuple
print(len(random_letters))

# todo: to count the number times the  elements in the tuple
print(random_letters.count('a'))

#! to find the index of the element in the tuple
print(random_letters.index("f"))

# * Convert typle into list
num_list = list(num_tuple)
print(num_list)

# * convert list into tuple
num_tuple = tuple(num_list)
print(num_tuple)

#! calculating stipend using tuple 
a = int(input('enter your monthly Stipend in dollar: ' ))
b = a
dollar = (a,b) #tuple5
print(type(dollar))

for value in dollar:
    monthy_Stipend_in_dollars = ((value*8)*5)*4
    converting_to_rupies =round(monthy_Stipend_in_dollars*72.99)
    print("Your Monthly stipend in Indian rupies: ",converting_to_rupies)

#* slicing tuple
slicing = (1,2,3,4,5,6,7,8,9) #tuple6
slicing_tuple = slicing[2:8] 
print(slicing_tuple)

#todo: value matching in tuple 
value_mathing_tuple = ("Ali",21,"Canada") #tuple7
name,age,canada = value_mathing_tuple #here matching values inside the tuple with multiple variables
""" 
[Important Note:-]
    todo: Number Variables you creating that should match the number of variables in Tuple.
    !: otherwise Error  will arrise.
"""
print(name,age,canada)

numericals = (1,2,3,4,5,6,7,8,9)
"""
[Important Note:-]
    !: i1 represents the first value in tuple.
    ?: i3 represents the last value in tuple.
    *: *i2 represents all remaining values which present after the first value and before the last value in tuple.
    todo: *i2 values will be printed inside the list.

"""
i1, *i2, i3 = numericals
print(i1,i3,i2)

#!comparing the size of list and tuple with same values
import sys
from time import time
init = time() #For Checking execution time
value_of_list = [0, 1, 2, "hello", True]
print(sys.getsizeof(value_of_list),"bytes",time()-init,"Time")
init = time() #for checking execution time 
value_of_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(value_of_tuple),"bytes",time()-init,"Time") 

#! comparing the execution time of the list and tuple with same values
import timeit
"""
[Important Note:-]
    ! stmt means Statemnt the values inside the stmt will printed.
    ! number = 1000000 means the value inside the stmt will be printed for 1000000 times.
    ! here we using timeit module to print 
"""

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))