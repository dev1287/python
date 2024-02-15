#/usr/bin/python3
"""
Leap year
"""
century = int(input("enter the century: "))

start_year = century * 100             #2000
end_year = start_year + 100            #2000 + 10

leap_years = []

for year in range(start_year, end_year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        leap_years.append(year)

print(f"Leap years in the {century}st century:")
print(leap_years)