"""
birthday.py
Author: Johari
Credit: megsnyder, noah 
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
mounth = month_name[todaymonth]


name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what was the name of the month you were born in?")
y = input("And what yoear were your born in, " + name + "? ")
d = input("And the day? ")
day = int(d) 
year = int(y)


if month == "October" and day == 31:
    print("You were born on Halloween!")
    
elif month == todaymonth and day == todaydate:
    print("Happy birthday!") 
    
elif month == "December" or month == "January" or month == "February" and year >= 1990 and year <= 1999:
    print ("You are a winter baby of the nineties. ")
    
elif month == "March" or month == "April" or month == "May" and year >= 1990 and year <= 1999 : 
    print("You are a spring baby of the nineties.")
    
elif month == "June" or month == "July" or month == "August" and year >= 1990 and year <= 1999:
    print("You are a summer baby of the nineties.") 
    
elif month == "September" or month == "October" or month == "November" and year >= 1990 and year <= 1999:
    print("You are a fall baby of the nineties.") 

elif month == "December" or month == "January" or month == "February" and year >= 1980 and year <= 1989:
    print ("You are a winter baby of the eighties.")
    
elif month == "March" or month == "April" or month == "May" and year >= 1980 and year <= 1989 : 
    print("You are a spring baby of the eighties.")
    
elif month == "June" or month == "July" or month == "August" and year >= 1980 and year <= 1989:
    print("You are a summer baby of the eighties.") 
    
elif month == "September" or month == "October" or month == "November" and year >= 1980 and year <= 1989:
    print("You are a fall baby of the eighties.") 

elif month == "December" or month == "January" or month == "February" and year >= 2000:
    print ("You are a winter baby of the two thousands.")
    
elif month == "March" or month == "April" or month == "May" and year >= 2000: 
    print("You are a spring baby of the two thousands.")
    
elif month == "June" or month == "July" or month == "August" and year >= 2000:
    print("You are a summer baby of the two thousands.") 
    
elif month == "September" or month == "October" or month == "November" and year >= 2000:
    print("You are a fall baby of the two thousands.") 
    
elif month == "December" or month == "January" or month == "February" and year < 1980:
    print ("You are a winter baby of the stone age.")
    
elif month == "March" or month == "April" or month == "May" and year < 1980: 
    print("You are a spring baby of the stone age.")
    
elif month == "June" or month == "July" or month == "August" and year < 1980:
    print("You are a summer baby of the stone age.") 
    
elif month == "September" or month == "October" or month == "November" and year < 1980:
    print("You are a fall baby of the stone age.") 
else:
    print("ok")

