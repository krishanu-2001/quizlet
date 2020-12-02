# importing the tkinter module and PIL 
# that is pillow module
import os
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox


def forward(img_no): 

	# GLobal variable so that we can have 
	# access and change the variable 
	# whenever needed 
	global label 
	global button_forward 
	global button_back 
	global button_exit 
	label.grid_forget() 

	# This is for clearing the screen so that 
	# our next image can pop up 
	label = Label(image=List_images[img_no-1]) 

	# as the list starts from 0 so we are 
	# subtracting one 
	label.grid(row=1, column=0, columnspan=3) 
	button_for = Button(root, text="forward", 
						command=lambda: forward(img_no+1)) 

	# img_no+1 as we want the next image to pop up 
	if img_no == 4: 
		button_forward = Button(root, text="Forward", 
								state=DISABLED) 

	# img_no-1 as we want previous image when we click 
	# back button 
	button_back = Button(root, text="Back", 
						command=lambda: back(img_no-1)) 

	# Placing the button in new grid 
	button_back.place(x = 70,y = 400)
	button_exit.place(x = 250,y = 400)
	button_for.place(x = 400,y = 400)


def back(img_no): 

	# We willl have global variable to access these 
	# variable and change whenever needed 
	global label 
	global button_forward 
	global button_back 
	global button_exit 
	label.grid_forget() 

	# for clearing the image for new image to pop up 
	label = Label(image=List_images[img_no - 1]) 
	label.grid(row=1, column=0, columnspan=3) 
	button_for = Button(root, text="forward", 
							command=lambda: forward(img_no + 1)) 
	button_back = Button(root, text="Back", 
						command=lambda: back(img_no - 1)) 
	print(img_no) 

	# whenever the first image will be there we will 
	# have the back button disabled 
	if img_no == 1: 
		button_back = Button(root, Text="Back", state=DISABLED) 

	label.grid(row=1, column=0, columnspan=3) 
	button_back.place(x = 70,y = 400) 
	button_exit.place(x = 250,y = 400) 
	button_for.place(x = 400,y = 400)


def submit():
	try:
		# the input provided by the user is
		# stored in here :temp
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		
		# divmod(firstvalue = temp//60, secondvalue = temp%60)
		mins,secs = divmod(temp,60) 

		# Converting the input entered in mins or secs to hours,
		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
		# 50min: 0sec)
		hours=0
		if mins >60:
			
			# divmod(firstvalue = temp//60, secondvalue 
			# = temp%60)
			hours, mins = divmod(mins, 60)
		
		# using format () method to store the value up to 
		# two decimal places
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		# updating the GUI window after decrementing the
		# temp value every time
		root.update()
		time.sleep(1)

		# when temp value = 0; then a messagebox pop's up
		# with a message:"Time's up"
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")
		
		# after every one sec the value of temp will be decremented
		# by one
		temp -= 1


# Calling the Tk (The intial constructor of tkinter) 
root = Tk() 
root.title("Image Viewer") 
root.geometry("700x700")

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=hour)
hourEntry.place(x=80,y=500)

minuteEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=minute)
minuteEntry.place(x=130,y=500)

secondEntry= Entry(root, width=3, font=("Arial",18,""),
				textvariable=second)
secondEntry.place(x=180,y=500)

pixels_x = 100
pixels_y = 100
# Adding the images using the pillow module which 
# has a class ImageTk We can directly add the 
# photos in the tkinter folder or we have to 
# give a proper path for the images
path = "quiz_photos/"
temp = os.listdir(path)
image_no_ = []
for i in range(len(temp)):
    image_no_.append(ImageTk.PhotoImage(Image.open("quiz_photos/" + str(temp[i]))) )
print(image_no_)

# List of the images so that we traverse the list 
List_images = image_no_

label = Label(image=image_no_[0]) 
# We have to show the the box so this below line is needed 
label.grid(row=1, column=0, columnspan=3) 

# We will have three button back ,forward and exit 
button_back = Button(root, text="Back", command=back, 
					state=DISABLED) 

# root.quit for closing the app 
button_exit = Button(root, text="Exit", 
					command=root.quit) 

button_forward = Button(root, text="Forward", 
						command=lambda: forward(1))

# grid function is for placing the buttons in the frame 
button_back.place(x = 70,y = 400) 
button_exit.place(x = 250,y = 400)
button_forward.place(x = 400,y = 400)

# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
			command= submit)
btn.place(x = 100,y = 550)

root.mainloop() 
