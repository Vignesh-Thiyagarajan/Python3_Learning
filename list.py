#LIST
car = ["creta","inova","nanao"] #list
print(car)

carlist = car[-3]  #saving list in variable
print(carlist)

for cars in car: #iterate in list
    print(cars)

if "inova" in car: #conditional if statement in list
    print("yes")
else:
    print("no")

print(len(car)) #using len we can check lenth of the list

car.append("bucati") #append will add elements at the end of list
print(car)

car.insert(1, "duster") #insert will add elements at the specific location that you  mentioned in a list
print(car)

car_s = car.pop() #pop will remove last element in the list
print(car_s)
print(car)

car_s = car.remove("duster") #remove is used to specific elements in list
print(car)

cars_s = car.reverse() #reverse is used to reverse elements in list (decending oder)
print(cars_s)
print(car)

cars_s = car.clear() #it will clear every element in the list
print(car)

num = [2,1,4,6,5,8,7,9]
print(num)

Sort_num = num.sort() #This Sort method will sort your original list
print(num)

num_2 = [2,1,4,6,3,5,8,7,9]
Sort_num2 = sorted(num_2) #This Sort method will not sort the original list
print(num_2,"Sorted List---->",Sort_num2)

num_3 = ["Your_Name"] * 5 #this method will create list with element you mentioned for number that you multiplied 
print(num_3)

First_Name = [input("First_Name: " )]
Last_Name = [input("Last_Name: " )]

Name = First_Name + Last_Name #concadinating elements or merging elements within your list
print(Name)

a = Sort_num2[1:7] #this will remove a elements before Start index and remove a elements after End index and assign the changes to the new list
print(a)

b = Sort_num2[::1] #::1 -> it will take every element in the list
print(b)

c = Sort_num2[::2] #::2 -> it only take every 2nd element in a list
print(c)

d= Sort_num2[::3] #::3 ->it will only take every 3rd elemts in a list 
print(d)

e= Sort_num2[::-1] #Reverse a list (Easy method)

bikes = ["honda","pulsar","Cbr"]
#? Don't Create a copy like this using bellow method
bikes_copy= bikes #! Here bike and bikes will use same memory location If you change anyone it will affect both. Then It will not create new copy of bikes in bikes_copy!!!
bikes_copy.append("tvs") 
print(bikes)
print(bikes_copy)

#todo:use below method make copy of list
bikes_copy2 = list(bikes) # *this wil create a original copy of bikes to bikes_copy2. both has seperate memory location!!!
bikes_copy2.append("Yamaha")
print(bikes_copy2)
print(bikes)

#todo:use below method also to make copy of list
bikes_copy3 = bikes[:] # *this wil create a original copy of bikes to bikes_copy3. both has seperate memory location!!!
bikes_copy3.append("hero")
print(bikes_copy3)
print(bikes)

num_list = [1,2,3,4,5,6,7,8,9,10]
ans = [number*number for number in num_list]
print(num_list)
print(ans) 

#! list comprehension (Its an advance topic in list)

num_list = [1,2,3,4,5,6,7,8,9,10]
ans = [number*number for number in num_list] #Todo: using this method we going to create a  new list with the Square of a number in existing list!!!
print(num_list) # here both list will have separate memory location!!!.
print(ans) 
