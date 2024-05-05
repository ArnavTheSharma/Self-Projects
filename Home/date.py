month = int(input('Enter month: '))
date1 = int(input('Enter date: '))
# year = int(input('Enter year: '))
diff = int(input('How many days do you want to go forward? '))
year_diff=diff/365
diff = diff%356

days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #number of days in each month in order
days2 = [0] #number of days that have passed from the start of the year (e.g. at feb28 31+28 days have passed)
j = 0
for i in days1:
    j += i
    days2.append(j)

date2 = days2[month-1] + date1 + diff #number of days that passed after adding days going forward 

days2.append(date2) 
days2.sort()

month2 = days2.index(date2)
date3 = date2 - days2[month2-1]
print(month2, date3)

