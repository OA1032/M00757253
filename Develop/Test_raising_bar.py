import opc # Necessary Library to run the 60x6 LED simulator 
import time # Time Library needed so sleeps time.sleep() is possible. Allowing short wwaits when decided within the code before executing the next line 

colour=[(0,0,0)]*360 # Set intial colour to all blank

client = opc.Client('localhost:7890') # needed to use the OPC for Strands 

def blinky():
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

    for i in range(60,30,-1):# decrement from set point
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