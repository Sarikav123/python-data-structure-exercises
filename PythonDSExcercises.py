#:List Exercise Q1. Create a list of 5 random numbers and print the list.


my_list = [2,5,7,9,23]
print( 'List values are :',my_list)

#Q2. Insert 3 new values to the list and print the updated list.

my_list.extend([4,78,89])
print('Updated List values are :',my_list)

#Q3. Try to use a for loop to print each element in the list.
print('List Items')
for i in my_list:
    print(i)


### Topic: Dictionary Exercise  ###

##Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

my_dict = { 'name':'John',
       'age':25,
       'address':'New York'
     }
print('Dictionary key pair values are', my_dict)
my_dict['phone'] =1234567890
print('Updated Dictionary key pair values are', my_dict)

#Topic: Set Exercise Q1.Create a set with values 1, 2, 3, 4, and 5.

my_set = {1,2,3,4,5}
print('The set values are', my_set)
#Q2. Add the value 6 to the set created in Q1.

my_set.add(6)
print('The set values are', my_set)

my_set.remove(3)
print('The set values are', my_set)


## Topic:Tuple Exercise Q1. Create a tuple with values 1, 2, 3, and 4

my_tuple = (1,2,3,4)

print("The tuple values are ", my_tuple)

# Q2. Print the length of the tuple created in Q1.

print("The length of tuple is " ,len(my_tuple))

##Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.