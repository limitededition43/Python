#!/usr/bin/python3 

# Ordered List
ListA = ["one",2,3,5,5,6,9,8,9]
ListB = ["one",2,3,5,5,6,9,8,9]

print("ListA =", ListA)
print("ListB =", ListB)

print("Both Lists in same order: " ,ListA == ListB)


#List can be modified

print("Current list A: " , ListA)					# value 1 is updated at index 0.
ListA[0] = 1
print("Updated list A: " , ListA)


#Methods

ListA.sort()
print("Sorting ListA: ", ListA)                 	                #By default does a alphabetic sort but should of same data type or can use sorted

ListA.append('monday')    						#appends a single newitem at the end.
print("Appending an item to list: " , ListA)

ExtendList = ["tuesday","wednesday",10]
ListA.extend(ExtendList)
print("Add multiple item to list: ", ListA)				#appends iterable items at the end

ListA.insert(1,"Inserteditem")
print("Insert an item at index 1: ", ListA)				#inserts into the list at index 1

print("Index position of item 5: ", ListA.index(5))			#Find index of given item

print("Count occurences of given value 9: " , ListA.count(9))		#Displays repetition of 9

ListA.pop(8)
print("Popping item from index 8: ", ListA)				#Removes item from index

ListA.remove("monday")
print("Removing item by value monday: ", ListA)				#Incase of duplicates, removes first match

Newlist = ListA.copy()							#Copies LisaA to Newlist
print("Copied newList from ListA :" , Newlist)

Newlist.clear()
print("After clearing:", Newlist)



#Nested Lists
print("Current ListB: ", ListB)						#Display items in ListB
ListB[1]= ["2.1","2.2","2.3"]           				#Lists can be an item within a list.
print("Updating new List within list at index 1: ", ListB)		#Shows updated list


#Accessing sublist
print("Value in sublist in index: ", ListB[1][2])       		#Accessing Nested Lists
