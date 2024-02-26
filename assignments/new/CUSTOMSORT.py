def c_sum(numbers):
    result = 0
    for item in numbers:
        result += item
    return result


numbers = [1, 2, 3, 4, 5]
print(c_sum(numbers))  #15