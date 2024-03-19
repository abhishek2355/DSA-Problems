# Program to check the year is leap year or not.

def checkYear(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif(year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input())
ans = checkYear(year)

if ans:
    print("Given year is the leap year.")
else:
    print("Given year is not the leap year.")