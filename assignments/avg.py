"""
calculating the average of numbers
"""

n = int(input("enter number of elements : "))  #2 
num = [int(input()) for _ in range(n)]         #2,3
avg = sum(num) / len(num)                      #5/2
print(f"Average of given numbers is : {avg}")  #2.5
