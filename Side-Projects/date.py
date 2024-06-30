# this code asks how many days you wanna go forward from a given date and returns a date

month = int(input('Enter month: '))
date = int(input('Enter date: '))
diff = int(input('How many days do you want to go forward? '))
diff = diff%365

#number of days in each month in order
days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

#this loop creates a list, day2, which tells the number of days that have passed from the start of the year (e.g. at feb20 31+20 days have passed)
days2 = []
j = 0
for i in days1:
    j += i
    days2.append(j)

# date2 tells the number of days that have passed for the ending date 
# (days2[month-1]) gives the number of days the current month has had since the start of the year
# we add the current date and how many days we want going forward on top of this
date2 = days2[month-1] + date + diff 

#add date2 to the list, days2, to figure out the new date's month
days2.append(date2) 
days2.sort()

#the index gives the month and the date is the difference between the current and previous index
month2 = days2.index(date2)
date3 = date2 - days2[month2-1]
print(month2, "/", date3)

