my_car1 = {"car_name": "Mahindra XUV700", "car_colour": "Red"} #dict1
print(my_car1)

my_car2 = dict(car_name="Creta", car_colour="White") #dict2
print(my_car2)

value = my_car2["car_name"] #! geting value of car_name from dict2 dictionary
print(value) 

my_car1["wheel_type"] = "Four Wheel Drive" #! adding Wheel_type key and Four wheel drive value to the dic1 dictionary
print(my_car1)

my_car1["wheel_type"] = "Two Wheel Drive" #todo: updating Two Wheel Drive value to the Wheel_type key in dic1 dictionary
print(my_car1)

del my_car1["wheel_type"] #? Deleting Wheel_type key and Two Wheel Drive value in dic1 dictionary
print(my_car1)

my_car2.popitem() #* popitem will remove last key and value from the dict2 dictionary
print(my_car2)

if "car_name" in my_car1: #! using if statement for checking elements in the dictionary
    print(my_car1["car_name"])
else:
    raise ValueError("key and value not found")

try: #! using try for checking elements in the dictionary
    print(my_car2["car_name"])
except:
    print("Error")

for key in my_car1.keys(): #for geting keys in the dictionary using for loop
    print(key)

for value in my_car1.values(): #for geting values in the dictionary using for loop
    print(value)

mycar1_cpy=my_car1 #! this will change both original and copy of dictionary.
mycar1_cpy["windows"] = "Two"
print(mycar1_cpy)
print(my_car1)

my_car2_cpy = my_car1.copy() #todo: this will not change the original dictionary.
my_car2_cpy.pop("windows") #? here windows key and its value are deleted.
print(my_car2_cpy)
print(my_car1) 

my_car3_cpy = dict(my_car1) #todo: this will not change the original dictionary.
my_car3_cpy.pop("windows") #? here windows key and its value are deleted.
print(my_car3_cpy)
print(my_car1)

clg = {"name": "JAYA", "palce": "Thiruninravur", "Course": "BCA"} #dict3
clg_2 = dict(name="Jaya College", place="Thiruninravur", email="jaya@gmail.com") #dict4

clg.update(clg_2)
print(clg)
name1= (input("Enter the name1: " ))
name2= (input("Enter the name2: " ))
rol_number = {0:name1,1:name2} #dict5 #!geting value from user for dictionary 
#rol_number = [0:name1,1:name2] #list1 #!list will not work as dictionoray because it will not support hashing.
print(rol_number)