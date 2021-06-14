
# General tuple packing 
tup = 1,2,3,4,5 
print("General Tuple but enclosed within paranthesis: " , tup)

# Tuples with paranthesis
tup =(1,2,3,4,5)
print("Tuple with paranthesis gives same output: " , tup)


#tuples with different data types
tup = (1,"string",True,3.14, b'0xdeedbeef',["1","2","3"],{1,2,3},{'a':1,'b':2})
for i in tup:
  print(type(i),"contains", i)

#print positional values from tuple with index
print("Index 0 and 1 contains: " , tup[0],"and",tup[1])

#Construct an empty tuple using tuple() and pass value to the empty tuple
tup = tuple()
print(tup, " is empty")

# must have atleast two values within a tuple
tup =(1)
print(type(tup))  #one value doesn't make it a tuple

tup =(1,)
print(type(tup))  #one value with a comma makes it a tuple.

#Some methods on tuple
tup = "Python", "Awesome", "Snake", 'is', 'not','is'
print("Length: ", len(tup))
print(tup[0],tup[3],tup[1])
print("Item not is located at:" ,tup.index("not"))   
print("Duplicate occurence of \"is\":", tup.count("is"))
# tup[0]= "Java" - > No assignment allowed (TypeError)

#Concatenate or merging
tup1=(1,2,3)
tup2=('a','b','c')
print("Tuple 1: ",tup1)
print("Tuple 2: ",tup2)  
print("Concatenate: ", tup1 + tup2)

#Get range of values from a tuple using slicing
tup =('first','second',3,4,'last')
print("New Tuple = " ,tup)
print("Slicing: ",tup[1:],tup[-1:]) #negative sign denotes reverse order
print(tup[2:],tup[-2:]) 

#Conditions
tup = "mon","tue","wed","thur","fri"
print("wed" in tup) #Check value is in tuple gives Boolean output


#packing
tup = (1,2,3)       #the tuple is packed into tup
a,b,c = tup         #items unpacked to variables
print(tup)
print("a,b,c unpackes and holds ",a,b,c)





