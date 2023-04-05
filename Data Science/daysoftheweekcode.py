
#Mr.Yu wanted me to be able to code out a project that let the user input "what day of the week is it" and "whats your least faveroite day of the week" and output everything but that day and yeah
import datetime

# use the library "datetime" to pull what the day is in real life
today = datetime.date.today()

# make the list of the weekdays and type them out so the dumb computer knows how to paste 
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#what is the least fav day of the week for the user and have them input it
least_favorite = input("What is your least favorite day? ")

#output every day but the least fav day that the user said
remaining_weekdays = [day for day in weekdays if day != least_favorite.capitalize()]

#pull the index of today's weekday in the weekdays list so that we can do what we want the code to
today_index = weekdays.index(today.strftime('%A'))

# paste remaing days of the week starting tommorow 
if today_index == 6: # if today is Sunday, start from Monday
  print("Tomorrow is a new week!")
  print("You still have", ', '.join(remaining_weekdays[0:5]), "this week")
else:
  print("You still have", ', '.join(remaining_weekdays[today_index+1:]), "this week")
