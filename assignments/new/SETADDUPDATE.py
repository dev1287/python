simple_set = {1, 2, 3}

# Using add
simple_set.add('tomato')
print("After add('tomato'):", simple_set) #{'tomato', 1, 2, 3}

# Using add again
simple_set.add('tomato')
print("After add('tomato'):", simple_set) #{'tomato', 1, 2, 3}

# Using update
simple_set.update('tomato')  
print("After update('tomato'):", simple_set) #{1, 2, 3, 't', 'a', 'apple', 'tomato', 'o', 'm'}


# Using update again
simple_set.update('tomato')  
print("After update('tomato'):", simple_set) #{1, 2, 3, 't', 'a', 'apple', 'tomato', 'o', 'm'}