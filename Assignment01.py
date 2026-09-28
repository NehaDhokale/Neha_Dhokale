#1. List Operations
my_list=[10,20,30,40]
print("Original List:", my_list)
my_list.append(50)
my_list.insert(1,15)
my_list.remove(30)
my_list.pop()
my_list.sort()
print("List after Operations:",my_list)

#2. Tuple Operations
my_tuple = (10,20,30,20,40)
print("\nOriginal Tuple:",my_tuple)
print("indexing[2]:", my_tuple[2])
print("silicing[1:4]:",my_tuple[1:4])
print("count of 20:" , my_tuple.count(20))
print("Index of 30:",my_tuple.index(30))
new_tuple = my_tuple+ (50,60)
print("After concatenation:", new_tuple)

#3. Dictionary Operations
student = {"name":"Rahul","age":18,"cource":"CSE"}
print("\nOriginal Dictionary:",student)
student["city"]="pune"             #add
student.update({"age":19})      #update
print("After adding and updating:",student)
print("keys:", student.keys())
print("values:",student.values())
print("items:",student.items())
student.pop("city")               #remove
print("After removing city:",student)
