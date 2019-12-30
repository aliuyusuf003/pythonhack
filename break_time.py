#This program reminds me to take a break\
import time
import webbrowser



current_time = time.ctime()

total_breaks = 2
break_count = 0


print("Pleas take a break as you have been sitting for about two hours ago till "+current_time)
while (break_count < total_breaks):
    time.sleep(7200)
    webbrowser.open('https://www.youtube.com/watch?v=6f9BABxOJIY')
    break_count += 1
