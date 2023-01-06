'''
ask user input for the following
	swimming_time
	cycling_time
	running_time
add them all up in triathlon_time variable

create conditional statements for the awards
if triathlon_time is less than or equal to 100 minutes
	print "You have been awarded the Provincial Colours."
elif triathlon_time is less than or equal to 105 minutes
	print "You have been awarded the Provincial Half Colours."
elif triathlon_time is less than or equal to 110 minutes
	print "You have been awarded the Provincial Scroll."
else
	print "You are not eligible for any awards."
'''

swimming_time = float(input("What is your swimming time (mins)? \n"))
cycling_time = float(input("What is your cycling time (mins)? \n"))
running_time = float(input("What is your running time (mins)? \n"))
# inputs for triathlon race
# deliberated on the use or int or float for this and decided that float would take into account wider range of inputs

triathlon_time = swimming_time + cycling_time + running_time
# total for time taken to complete the triathlon

# using of f"" and /n makes the outlook look simple and clean. 
if triathlon_time<=100:
    print(f"You completed the triathlon in {triathlon_time} minutes.\nYou have been awarded the Provincial Colours award.")
elif triathlon_time<=105:
    print(f"You completed the triathlon in {triathlon_time} minutes.\nYou have been awarded the Provincial Half Colours award.")
elif triathlon_time<=110:
    print(f"You completed the triathlon in {triathlon_time} minutes.\nYou have been awarded the Provincial Scroll award.")
else:
    print(f"You completed the triathlon in {triathlon_time} minutes.\nYou are not eligible for any award.")