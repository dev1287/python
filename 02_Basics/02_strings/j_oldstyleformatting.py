#!/usr/bin/python3

#!/usr/bin/python3
"""
Purpose: String Formatting
            - Types
                1. Old Style formatting (or literal formatting)
                2. New Style formatting
                3. F-Strings  ( works from python 3.6+)

OLD-Style formatting
    %d - integer
    %i - integer

    %c - single char
    %s - string/char

    %f - floating-point
    %F - floating-point

    %o - octal
    %x - hexadecimal lowercase
    %X - hexadecimal uppercase

"""
print()
print("in old formatting style we use tell int or float will come in advance if it changes it gives error")
print("%d is intiger")
print("" % ())
print("the number here is %d")          #the number here is %d
print("the number here is %d" %(10))    #the number here is 10
print("the number here is %d" %10)      #the number here is 10
print("the number here is %d" %11.87)   #the number here is 11 (11.87 float is coverted to 11 at output)
#print("the number here is %d" %'99.87') #%d format: a real number is required, not str  (it shows error staying we cant give strings)


print("after . six decimals will be there")
#("the float here is %f" % "12")    # must be real number, not str
print("the float here is %f" % 12.34)   # 12.340000
print("the float here is %f" % 12)      # 12.000000
print("the float here is %f" % False)   # 0.000000
print()
print()
print("string not throw any error")  # str()
print("the string here is %s" % True) #the string here is True
print("the string here is %s" % None) #the string here is None
print("the string here is %s" % 1)    #the string here is 1
print("the string here is %s" % 1.9) #the string here is 1.9
print("the string here is %s" % 4545) #the string here is 4545
print("the string here is %s" % "python")  #the string here is python
print()
print()
print("in backend it uses repr() function repr will add extra string that is only difference") #repr()
print()
print()  # repr()
print("the repr string is %r" % True)
print("the repr string is %r" % None)
print("the repr string is %r" % 1)
print("the repr string is %r" % 1.9)
print("the repr string is %r" % 4545)
print("the repr string is %r" % "python") # it add extra quote to python when compared to %s
print()
print()  # repr()
print()
print()

print("%o" % 100, oct(100)) # %o - octal
print("%x" % 100, hex(100)) # %x - hexadecimal lowercase
print("%X" % 100, hex(100)) # %X - hexadecimal uppercase
#%b - binary
#print('%b' % (12), bin(12)) #ValueError: unsupported format character 'b' (0x62) at index 1
print()
print()

print()
print("%s" % "100")
print("%c" % "1") #for single character it throws error more than one character
print("%s" % "1")
print()
print()  # float()  -- 6 digits post decimal
print("%f" % 87.34)  # 87.340000 
print("%F" % 87.34)  # 87.340000
print("%F" % 87.65458533344)  # 87.654585 (even giving big decimal it gives only6)
print()
print("below tries to round of a value")
print()
print("%g" % 87.34)  # 87.34
print("%G" % 87.34)  # 87.34
print("%G" % 87.34223123123123)  # 87.3422
print()

print()
print()
print("%e" % 8.34)  # 8.34000e+00
print("%E" % 8.34)  # 8.34000E+00
print("%E" % 8.65458533344)  # 8.654585E+00

print()
print()
import math

print(math.pi)  # 3.141592653589793
print("%d" % math.pi)       # 3 (converting to integer)
print("%f" % math.pi)       # 3.141593 (only 6 decimals)
print("%9f" % math.pi)      #  3.141593 (space before 3 as it contains 9)
print("%9.3f" % math.pi)    #     3.142  ( we are reserving 9 digits,4 space before,3 decimals)

###################################################
print()
print()
print("the number is %d only." % 786)  # the number is 786 only.
print("pi value is %f!!!" % 3.1416) #pi value is 3.141600!!
print("pi value is %10f!!" % 3.1416) #pi value is   3.141600!!
print("pi value is %10.3f!!" % 3.1416) #pi value is      3.142!!
print("pi value is %010.3f!!" % 3.1416) #pi value is 000003.142!!
 
print("my name is %s - %s." % ("raghavendra", "rav"))
print()
print()

print("My name is %s. I am %d old paying a tax of %f")
print("My name is %s. I am %d old paying a tax of %f" % ("raghavendra", 29, 15.5))

# print('My name is %s. I am %d old paying a tax of %f' % ('raghavendra', '29', 15.5))
# TypeError: %d format: a real number is required, not str

print()
print()
print("My name is %r. I am %r old paying a tax of %r" % ("raghu", "33", 15.5))
print("My name is %s. I am %s old paying a tax of %s" % ("raghu", "33", 15.5))
# we need to match same no of values

# print('My name is %s. I am %s old paying a tax of %s' % ('raghu', 15.5))
# TypeError: not enough arguments for format string
print()
print(
    "%(language)s has %(My favourite number)03d quote types."
    % {"language": "Python", "My favourite number": 9}
)

print()
print()
print("2".zfill(9))  # '000000002'
print("%03d" % 9)  # '009'
print("%3d" % 9)  # '  9'


# Limitations of old style string formatting
# 1. same data types need to be passed
# 2. If same value need to go more than one time,
#     those many number of times, values need to be passed
