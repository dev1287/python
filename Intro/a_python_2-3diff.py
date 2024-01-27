print ("hello")
print(1+0)
print(1*0)
#it shows error

try:
    print(1/0)
except Exception as ex:
    print("An execption occured this custom error", ex)
