list2 = [1, 11, 111]
print(type(list2))
value =int(input("Enter the value to append: "))
list2.insert(0, value) #0,3
print(list2)
print("length is:", len(list2))
list2.pop()
print(list2)
print("length is:",len( list2))