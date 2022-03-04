# importing necessary modules and libraries for the code to function.
import opc # library used for simulator
import time # time library for sleeps 
from colourdict import * #import all of the dictionary I created 
import random # library for random
 #GUi library as an abbreviated variable name 

colour=[(0,0,0)]*360 #intialising the 360LEDs at RGB value (0,0,0)['black']

client = opc.Client('localhost:7890') # connecting to the simulator 

c1 = random.choice(list(colourdict.values())) # Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c1)

c2 = random.choice(list(colourdict.values()))# Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c2)

c3 = random.choice(list(colourdict.values()))# Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c3)

c4 = random.choice(list(colourdict.values()))# Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c4)

c5 = random.choice(list(colourdict.values()))# Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c5)

c6 = random.choice(list(colourdict.values()))# Random Tupels from the colour dictionary (this is getting a random value from the keys values dictionary pair)
print(c6)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags__Horizontal_Slow_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an1(): # define function 
    for i in range(0,360): #Iterate through all of the LED's
        #Led printing starting point
    # if led = range()# do for colours
        #colour[i] =(0,0,0) # set led to 'black'
        client.put_pixels(colour)# sends signal to simulator
        time.sleep(0.05)# short wait 
        if i >= 0 and i < 60:       # conditional for 1st row of LED's
            colour[i] = c1  # random tuple of three values to decide colour in the form of RGB
        if i >= 60 and i < 120:     # conditional for 2nd row of LED's
            colour[i] = c2  # random tuple of three values to decide colour in the form of RGB
        if i >= 120 and i < 180:    # conditional for 3rd row of LED's
            colour[i] = c3  # random tuple of three values to decide colour in the form of RGB
        if i >= 180 and i < 240:    # conditional for 4th row of LED's
            colour[i] = c4    # random tuple of three values to decide colour in the form of RGB
        if i >= 240 and i < 300:    # conditional for 5th row of LED's
            colour[i] = c5  # random tuple of three values to decide colour in the form of RGB
        if i >= 300 and i <= 360:    # conditional for 6th row of LED's
            colour[i] = c6  # random tuple of three values to decide colour in the form of RGB
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Vertical_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an2():  #defining a function 
    #Inverse_Nigeria currently
    for i in range(11,50,1): # setting iteration boundries (start,stop,step)
        if i >= 10 and i < 24: #setting conditional positional boundries for the LED's
            colour[i] =(255,255,255) # set colour of LEDs in position i
            client.put_pixels(colour)
            print("i =",i)#Positional check of loop iterator

        if i >= 24 and i <= 37: #setting conditional positional boundries for the LED's
            colour[i] =(0,255,0)# set colour of LEDs in position i
            client.put_pixels(colour)
            print("i =",i)#Positional check of loop iterator

        if i >= 37 and i < 52: #setting conditional positional boundries for the LED's
            colour[i] =(0,255,0)# set colour of LEDs in position i
            client.put_pixels(colour)
            print("i =",i)#Positional check of loop iterator
        for x in range(i,360,60):
        #print vertically down
            time.sleep(0.1)
            if x >= 70 and x < 84 or (x >= 130 and x < 144) or (x >= 190 and x < 204) or (x >= 250 and x < 264)or (x >= 310 and x < 324): #setting conditional positional boundries for the LED's
                colour[x] =(255,255,255)# set colour of LEDs in position x
                client.put_pixels(colour)
                #time.sleep(0.1)
                print("Left =",i)#Positional check of loop iterator
            
            if (x >= 25 and x < 37) or (x >= 84 and x < 97) or (x >= 144 and x < 157) or (x >= 204 and x < 217)or (x >= 264 and x < 277) or (x >= 324 and x < 337): #setting conditional positional boundries for the LED's
                colour[x] =(0,255,0)# set colour of LEDs in position x
                client.put_pixels(colour)
                time.sleep(0.1)#small wait 
                print("Middle =",x)#Positional check of loop iterator

            if (x >= 37 and x < 50) or (x >= 97 and x < 110) or (x >= 157 and x < 170) or (x >= 217 and x < 230)or (x >= 277 and x < 290) or (x >= 337 and x < 350):#setting conditional positional boundries for the LED's
                colour[x] =(255,255,255)# set colour of LEDs in position x
                client.put_pixels(colour)
                print("Right =",x)#Positional check of loop iterator
                if x > i:  #if x is greater than the iterator of the loop it is within 
                    print("x =",x)# Positional check in the prints

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_1st_Line_Vertical_Horizontal_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an3():#Define a function 
    for i in range(10,51,1):#Loop parameters 
        #Led printing stating point
        #if led = range()
        colour[i] =(0,255,255)#RGB colour values 
        client.put_pixels(colour)
        time.sleep(0.5)#small wait 
        print("i =",i)#Positional check of loop iterator
        for x in range(i,361,60):#Nested loop parameters 
            #print vertically down
            if x > 60: #if x is
                colour[x] =(0,255,255) #RGB colour values 
                client.put_pixels(colour)
                if x > i:  #if x is greater than i 
                    print("x =",x)#positional check 
                    #No sleeps = new animation
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(HalfSlow_HalfFAST)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an4():# define a function below 
    for i in range(10,51,1):#Loop parameters (start, stop, step) #Led printing stating point
        print("i =",i)#Positional check of loop iterator
        for x in range(i,361,60):#Nested loop parameters (start, stop,step)
            #print vertically down
            #if led = range()
            colour[x] =c2 #Random colour tuple from colour dictionairy 
            client.put_pixels(colour)
            if 180 > x:  #if conditionals 
                time.sleep(0.2)#small wait
                print("x =",x)# nested loop positional check 
                #No sleeps = new animation

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Horizontal_print_Downwards~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an5():# function parameters below 
    for i in range(0,360): # iterate through all the LEDs from 0-360
        #Led printing stating point
        #if led = range()
        colour[i] =(0,255,255)#Positional check of loop iterator
        client.put_pixels(colour)
        #print("i =",i)
        if i == 59 or i ==119 or i == 179 or i == 239 or i == 299: # Multiconditional statement to determine when the sleeps take place 
            time.sleep(1)#small wait 
            print('sleep')#functionality check using printed string 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Vertical_Print_Sideways~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an6():# Function paramenter title
    for i in range(10,51,1): # Loop parameters 
        #Led printing starting point
        #if led = range()
        print("i =",i)#Positional check of loop iterator
        for x in range(i,361,60): # Nested loop parameters 
        #print vertically down
        #if led = range()
            colour[x] =(0,255,255) # RGB colour values 
            client.put_pixels(colour)    
            if x > i:  
                print("x =",x)#Positional check of loop iterator
                #time.sleep(0.01)
        if x > 300: # when x exceeds 300 do what is below 
            time.sleep(0.2)# small wait 
            print('sleep') # functionality check using strings 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Incomplete~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an7(): # Incomplete function 
    drop = [117,116,115,114,179,178,177,176,175,174,173,237,236,235,234] # water droplet list location
   
    for i in range(10):
        for water in drop:
            time.sleep(0.01)
            colour[water-i*5] =(0,0,255) 
            client.put_pixels(colour)
            print(water)
        print ("this is i" ,i)
        if water > 0 and water < 60:
            break

        for x in range(0,247):
            time.sleep(0.01)
            colour[x] =(0,0,0) 
            client.put_pixels(colour)
            print("deletion",x)
    
    if colour[x] == 60 or colour[x] == 120 or colour[x] == 180 or colour[x] == 240:
        time.sleep(0.1)


            





    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Dribble_Line_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an8():#define function 
    inc = 0#initialize inc variable value 
    loop = 0#initialize loop variable value 
    for i in range(3):# Loop parameters 
        for i in range(10,51): # loop parameters (start, stop, step)
            print(i) # Positional check
            #turn led on
            colour[i] =c1   #Random colour from colour dictionary in position i 
            client.put_pixels(colour)
            
            colour[i-1] =(0,0,0) #turn the LED in the previous position to 'black'
            client.put_pixels(colour)
            time.sleep(0.1)# small wait

            for x in range(i+60): #Nested loop parameters, loop one row below directly under position i 
                x = i + 60*inc #multiply the position of i by the inc to decide what row x will be in underneath i
                colour[x] =c3 #Random value tuple for colour value 
                client.put_pixels(colour)
                if x == x:# if x equals itself 
                    break # move on to the next code block
            print("x =",x)# Positional check 
        inc = inc + 1 # incrementing variable increments every time the loop finishes
        print ("inc =",inc) #Incrememnt check 
        if i == 50: # when i is equal to 50
            for i in range (50,9,-1):#Loop parameters, Decrement the count when if conditions are met
                print (i)#iterator positional check 
                #print reverse down
                colour[i] =c4 #Random dictionary value tuple(random colour)
                client.put_pixels(colour)
                time.sleep(0.1)#small wait
                if inc < 5:    
                    #turn off previous led 
                    colour[i] =(0,0,0)
                    client.put_pixels(colour)
                for x in range(i):#nested loop parameters 
                    x = i + 60*inc # making sure x is in a different row that depends on the increment value 
                    colour[x] =c6#Random dictionary value
                    client.put_pixels(colour)
                    print("x = ", x)# positional check
                    if x == x:#when x equals itself 
                        break#if the conditions are met break loop 
                    #time.sleep(0.1)
            inc = inc + 1 #inc increments whenever code above is executed in its entirety 
            print ("inc =",inc)#inc value check
        if i == 10 or i == 50: # conditional statement that triggers loop incrementation
            loop = loop +1 # Loop increments every time the code above executes entirely 
            print ("loop = ",loop)#Loop value check 
            # increment 6 times 
            ##need to add vertical print 
            #downwards with deletion occruring in line with inrement number
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Multi_Section_Wipe_vertical_flag_building~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an9():#Define function
    for i in range (300,360): # For loop to intiate a count on then bottom row of LEDs 
        print ("i",i) # Print check 
        colour[i] =(0,255,255) # RGB colour balance max blue and green colour values. 
        client.put_pixels(colour) # needed to update the simulator after every change 
        if i % 2 != 0: # conditional so only the even number of the LED's are affected by this 
            for x in range(i,i-360,-60): # Deecrement from the right side of the bottom row to the left starting at i stopping at i-360 and stepping by 60
                print("x",x) # Random variable in the nested for loop using a different assigned variable name.
                colour[x] =(0,255,255) # use this variable to and assign this set of colours to them 
                client.put_pixels(colour)# update the simulator 
                time.sleep(0.06)# pause for a short period of time 
        else: # if the value is odd the do this
            for x in range(i,i-360,-60):# Deecrement by 60 with a start of i a stop of i-360
                print("x",x)# assigned variable 
                colour[x] =(0,255,0)#make the colour Green 
                client.put_pixels(colour)#update the simulator
                time.sleep(0.06)# wait for a very short time.
        # time.sleep(0.1)

    for i in range(0,30):#increment from the left of the first row to midwayish 
        print("i",i)#check the count 
        colour[i] = (0,0,0)#turn the LED's at point i off 
        colour[i+60] = (0,0,0)#Do the same for the row above i
        colour[i+120] = (0,0,0)#Do the same for 2 rowa above i
        client.put_pixels(colour)#update the sumulator every time those 3 rows are turned off
        time.sleep(0.05)#stop for a short period of time
        
    for i in range(359,330,-1):# Decrement from the end of the LEDs
        print("i",i)#assigned variable 
        colour[i] = (0,0,0)#Turn LEDs off in position i 
        colour[i-60] = (0,0,0)#Turn LEDs off in position below i 
        colour[i-120] = (0,0,0)#Turn LEDs off in position two LED's below i 
        client.put_pixels(colour)#update the simulator
        time.sleep(0.05)#wait for a short time 
        
    for i in range(180,210):#count from the centre outwards in the simulator 
        print("i",i)#assigned variable 
        colour[i] = (0,0,0)#Turn LEDs off in position i
        colour[i+60] = (0,0,0)#Turn LEDs off in position above i
        colour[i+120] = (0,0,0)#Turn LEDs off in position two LED's above i
        client.put_pixels(colour)#Update the simulator
        time.sleep(0.05)#Wait for a short time 

    for i in range(60,30,-1):#decrementing loop
        print("i",i)#assigned variable 
        colour[i] = (0,0,0)#Turn LEDs off in position i
        colour[i+60] = (0,0,0)#Turn LEDs off in position above i
        colour[i+120] = (0,0,0)#Turn LEDs off in position two LED's above i
        client.put_pixels(colour)#Update the simulator
        time.sleep(0.05)#Wait for a short period of time 

    for i in range (143,158): #Count 15 LEDs in a straight uninterrupted line 
        print(i)#assigned variable 
        colour[i] =(0,255,0)#RGB balance of LEDs, 'i' turns Green
        client.put_pixels(colour)# update simulator 
        time.sleep(0.05)#short wait 

    for i in range(360):#iterate through all of the LED's
        if i % 2 == 0:#If the numerical position of the LED is divisible by two with a remainder of Zero do this.
            print ("i",i)#assigned variable 
            colour[i] =(0,255,0)#Turn the LED in position 'i' the colour of the selected RGB balance 
            colour[i+1] =(0,255,0)#Turn the LED in front of the LED in position 'i' the colour of the selected RGB balance 
            client.put_pixels(colour)#Update the simulator 
            time.sleep(0.05)#Wait a short amount of time 
        
            if i % 4 == 0:#If the numerical position of 'i' is divisible by 4 with a remainder of zero do this.
                print ("i",i)# assigned variable 
                colour[i] =(0,0,0)# Turns the LED at position 'i' off  
                colour[i+1] =(0,0,0)# turns the LED in front of the LED at position 'i' off
                client.put_pixels(colour)# Update the simulator 
                time.sleep(0.05)#Wait a short amount of time 

    for i in range(360):#Count through all of the LEDs
        print("i",i)#assigned variable 
        colour[i] =(0,0,0)#Turn LEDs off 
        client.put_pixels(colour)#Update simulator 
        if  i == 59 or i == 119 or i == 179 or i == 239 or i == 299:# Multiconditional if statements to ensure that after a row is turned off there is a pause 
            print("i",i)#assigned variable
            time.sleep(0.5)#Short wait 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Right_and_left_brought_together~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def an10():#Does not function 
    for i in range(10,30):# Loop parameters 
        print("i",i)#position check 
        colour[i] =(255,215,0)# LED row
        colour[i+60] =c6# LED row
        colour[i+120] =c6# LED row
        colour[i+180] =c6# LED row
        colour[i+240] =c6# LED row
        colour[i+300] =c6# LED row
        client.put_pixels(colour)
        time.sleep(0.1)#Small pause
        x = 59 - i# get x to decremeent as i increases 
        print("x",x) #Position checker 
        colour[x] =(255,215,0) # LED colour
        colour[x+60] =c4# LED row
        colour[x+120] =c4# LED row
        colour[x+180] =c4# LED row 
        colour[x+240] =c4# LED row
        colour[x+300] =c4# LED row
        client.put_pixels(colour)
#~~~~~~~~~~~~clear function~~~~~~~~~~~
def clearsim():#defining function 
    for i in range(360):#iterates through the whole simulator
        colour[i] =(0,0,0)# sets LEDs to 'black'
        client.put_pixels(colour)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Arduino~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import serial  # if missing in the command prompt or terminal  python-pip install pyserial
## Arduino code(Serial.available() > 0) {
# incomingByte = Serial.read()
# if incomingByte is string;
#       display string on LCD somehow
# }
# 
def arcomms():#function to establish arduino python connection 
    arduino = serial.Serial('COM3',9600)# port that then arduino is plugged into and the serial command 
    time.sleep(2)#short pause

    #exaple for multiple input
    # pot1,pot2, ldr = int(data.split(',')) # "255,204,0" = ["255","204","0"] = [255,204,0]

    def send_to_arduino(data):#define function for reading thne arduino data 
        arduino.write(str(data).encode('bytes'))#data in bytes

    while True:#while loop
        data = int(arduino.readline().decode('utf-8'))# work for default println behaviour. use str() if you are sending large datasets
        print(data)#print written data

        # within the folder, puthon filename.py

    sent_to_arduino()# run function 
#Do something when particular data comes through 
#~~~~~~~~~~~~tKinter~~~~~~~~~~~
from tkinter import * #tkinter library  

root = Tk() #intialize root window 
root.title("Animations") #Title string 
root.geometry("400x450") #Window size (x,y)
root.configure(bg='light grey') # set background colour

def hello(): #define function that prints hello
    print("hello")#print hello

def myClick():#function creation 
    myLabel = Label(root, text = "Hello " + e.get())#when label is pressed 
    myLabel.pack() #packs what is put onto screen as label

e = Entry(root, width = 50)#allow the user to type
e.pack()# auto size
e.insert(0, "Enter name here: ")# pre-entered text to indicate where to type

myButton = Button(root, text = "Animation 1",fg='white',bg='black',activebackground='orange',activeforeground='black',width=350,command = an1).pack()#defining the button parameters
myButton2 = Button(root, text = "Animation 2",fg='white',bg='black',activebackground='orange',activeforeground='black' ,width=350, command = an2).pack()#defining the button parameters
myButton3 = Button(root, text = "Animation 3",fg='white',bg='black',activebackground='orange',activeforeground='black' ,width=350, command = an3).pack()#defining the button parameters
myButton4 = Button(root, text = "Animation 4" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an4).pack()#defining the button parameters
myButton5 = Button(root, text = "Animation 5" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an5).pack()#defining the button parameters
myButton6 = Button(root, text = "Animation 6" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an6).pack()#defining the button parameters
myButton7 = Button(root, text = "Animation 7" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an7).pack()#defining the button parameters.This button is DISABLED due to the animation being incomplete
myButton8 = Button(root, text = "Animation 8" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an8).pack()#defining the button parameters
myButton9 = Button(root, text = "Animation 9" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an9).pack()#defining the button parameters
myButton10 = Button(root, text = "Animation 10" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = an10).pack()#defining the button parameters.This button is DISABLED due to the animation being incomplete
myButton11 = Button(root, text = "Click For Greeting!" ,fg='black',bg='green',width=350, command = myClick).pack()#defining the button parameters
myButton12 = Button(root, text = "Arduino Control" ,fg='white',bg='blue',width=350, command = arcomms,state = DISABLED).pack()#defining the button parameters. This button is DISABLED due to the animation being incomplete
myButton13 = Button(root, text = "Clear Simulator" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, command = clearsim).pack()#defining the button parameters
myButton14 = Button(root, text = "SELF DESTRUCT" ,fg='white',bg='red',activebackground='yellow',activeforeground='black',width=350, command = root.destroy).pack()#defining the button parameters
myButton15 = Button(root, text = "Coming Soon!" ,fg='white',bg='black',activebackground='orange',activeforeground='black',width=350, state=DISABLED).pack()#defining the button parameters.This button is DISABLED due to the animation being incomplete
#myButton14.bind()#defining the button parameters

root.mainloop()
