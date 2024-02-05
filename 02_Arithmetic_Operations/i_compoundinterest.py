borrowed_amount = int(input("Enter Borrowed Amount:"))
rate_of_interest = float(input("Enter Rate of Interest :")) / 100
loan_duration = int(input("Enter loan duration (in years):"))
# ** compound interest
payable_amount  = borrowed_amount * (1 + (rate_of_interest))**loan_duration
interest_amount = payable_amount - borrowed_amount
print("Principle          :", borrowed_amount)
print("Rate of Interest   :", rate_of_interest)
print("Loan Duration      :", loan_duration)
print("Interest amount    :", interest_amount)
print("total amount to pay:", payable_amount)
