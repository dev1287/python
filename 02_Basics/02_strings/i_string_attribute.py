#!/usr/bin/python3

"""
purpose: string operations

"""
#   ipython

#name = "python"

#name
#Out[2]: 'python'

#In [3]: type(name)
#Out[3]: str

#In [4]: name.zfill(7)
#Out[4]: '0python'

#In [5]: name.zfill(9)
#Out[5]: '000python'

#In [6]: name.zfill(3)
#Out[6]: 'python'

#In [7]: name.zfill(6)
#Out[7]: 'python'

#zfill will fill on the left
print ("42".zfill(5)) #outpot is 00042 zfill will replace with three zero before the number

print ("-92".zfill(5)) #output is -0042
print ("4-2".zfill(5)) #004-2
#old style string formatting
print("%05d" % (52))  #00052
print("%5d" % (52))   #   52
print("%-5d" % (87))  #87   it is not placing zeros after because it change sthe value and becomes 87000 instead of 87
print("%+5d" % (87))  #  +87 
print("%-05d" % (87)) #87 
#print("%05d" % ("hell"))  #TypeError: %d format: a real number is required, not str  (show error is string)

#center string
print("python class09".center(30)) #'      python class09     ' (places  in center)
#"python class09".center(30) '------python class09-----'
print("python class09".center(30,"-")) #'------python class09-----' (places spaces with -)
print("python class09".center(30,"*"))
print("python class09".center(30,"-"))
print()
print()
print("align the text to right")
print("python class09".rjust(30))     #                python class09
print("python class09".rjust(30,"-")) #----------------python class09
print("python class09".rjust(30,".")) #................python class09
print()
print()
print("align text to left")
print("python class09".ljust(30))     #python class09
print("python class09".ljust(30,"-")) #python class09----------------
print("python class09".ljust(30,".")) #python class09................
print()
print()


