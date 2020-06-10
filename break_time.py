#imports
import time
import webbrowser


"""
This code will open of a great song every couple of hours just to make sure you get a break
"""

#initial
total_breaks = 3
break_count = 0

#the bizness
while break_count < total_breaks:
    time.sleep(60*60*2)
    webbrowser.open("https://www.youtube.com/watch?v=cwqhdRs4jyA")
    break_count = break_count + 1
