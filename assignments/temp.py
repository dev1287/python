#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit


farhenheit = (1.8 * celsius) + 32  # PEMDAS

Algorithm:
step 1: take celcius , clear and validate 
step 2: convert and give farhenheit
"""

temp_input = input("enter the temperature: ").strip()
if temp_input[-1].lower() == "f": 
    temp = float(temp_input[:-1])
    celsius = (temp - 32) * 5/9
    print(f"Temperature is {round(celsius, 2)} C")
else:
    temp = float(temp_input)
    fahrenheit = (1.8 * temp) + 32
    print(f"Temperature is {round(fahrenheit, 2)} F")