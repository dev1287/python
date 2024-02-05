#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""
balance = input("Enter balance:")
balance = int(balance)
print("balance:", balance)
initial_deposit = input("Enter initial deposit:")
initial_deposit = int(initial_deposit)
salary_credited = input("salary credited amount:")
salary_credited = int(salary_credited)
online_purchase = input("online purchase amount:")
online_purchase = int(online_purchase)
house_rent = input("enter house rent:")
house_rent = int(house_rent)
current_balance=balance+initial_deposit+salary_credited-online_purchase+house_rent
print("updated balance:", current_balance)
