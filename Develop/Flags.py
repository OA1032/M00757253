#Set LED to black (Background)
#Test colours for LEDS (Black ,White,Red,Green,Blue)
#Import necessary libraries
#Use client put pixels when making various colour changes 
#make into functions
#Add a colour dictionairy
#diagonals = i+62/b -58 (60 +/- gap depending on direction)
'''make if statement with multiconditional for the 
colours of the flag and led position in each row
MAybe make it a function so it doesnt have to be repeated constaantly
most likely will have to do so for each individual flag..... RIP'''
import opc
import time

colour=[(0,0,0)]*360

client = opc.Client('localhost:7890')

   # new_colour =(r,g,b)
   #client.put_pixels(colour)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags__Horizontal_Slow_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''''for i in range(0,360):
    #Led printing starting point
   # if led = range()# do for colours
        colour[i] =(0,255,255)
        client.put_pixels(colour)
        time.sleep(0.1)
        make if statement with multiconditional for the 
        colours of the flag and led position in each row'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Vertical_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''#Inverse_Nigeria currently
for i in range(11,50,1):
    #time.sleep(0.1)
    if i >= 10 and i < 24: 
        colour[i] =(255,255,255)
        client.put_pixels(colour)
        print("i =",i)

    if i >= 24 and i <= 37: 
        colour[i] =(0,255,0)
        client.put_pixels(colour)
        #time.sleep(0.1)
        print("i =",i)

    if i >= 37 and i < 52: 
        colour[i] =(0,255,0)
        client.put_pixels(colour)
        #time.sleep(0.1)
        print("i =",i)
    for x in range(i,360,60):
    #print vertically down
        #if x > 60:
        time.sleep(0.1)
        if x >= 70 and x < 84 or (x >= 130 and x < 144) or (x >= 190 and x < 204) or (x >= 250 and x < 264)or (x >= 310 and x < 324): 
            colour[x] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            #time.sleep(0.1)
            print("Left =",i)
        
        if (x >= 25 and x < 37) or (x >= 84 and x < 97) or (x >= 144 and x < 157) or (x >= 204 and x < 217)or (x >= 264 and x < 277) or (x >= 324 and x < 337): 
            colour[x] =(0,255,0)
            client.put_pixels(colour)
            client.put_pixels(colour)
            time.sleep(0.1)
            print("Middle =",x)

        if (x >= 37 and x < 50) or (x >= 97 and x < 110) or (x >= 157 and x < 170) or (x >= 217 and x < 230)or (x >= 277 and x < 290) or (x >= 337 and x < 350):
            colour[x] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            #time.sleep(0.1)
            print("Right =",x)
                #colour[x] = (0,255,255) 
                #client.put_pixels(colour)
            if x > i:  
                print("x =",x)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_1st_Line_Vertical_Horizontal_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for i in range(10,51,1):
    #Led printing stating point
    #if led = range()
        colour[i] =(0,255,255)
        client.put_pixels(colour)
    print("i =",i)
    for x in range(i,361,60):
    #print vertically down
    if x > 100: 
        sleep(0.1)
    #if led = range()
        colour[i] =(0,255,255)
        client.put_pixels(colour)
        if x > i:  
            print("x =",x)
            #No sleeps = new animation'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Horizontal_print(FAST)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for i in range(10,51,1):
    #Led printing stating point
    #if led = range()
    print("i =",i)
    for x in range(i,361,60):
        #print vertically down
        #if led = range()
        colour[i] =(0,255,255)
        client.put_pixels(colour)
        if x > i:  
            print("x =",x)
            #No sleeps = new animation'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Horizontal_print_Downwards~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for i in range(0,360):
    #Led printing stating point
    #if led = range()
        colour[i] =(0,255,255)
        client.put_pixels(colour)
    #print("i =",i)
    if i == 60 or i ==120 or i == 180 or i == 240 or i == 300:
        time.sleep(0.1)
        print('sleep')'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Vertical_Print_Sideways~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for i in range(10,51,1):
    #Led printing starting point
    #if led = range()
    print("i =",i)
    for x in range(i,361,60):
    #print vertically down
    #if led = range()
        colour[i] =(0,255,255)
        client.put_pixels(colour)    
        if x > i:  
            print("x =",x)
    if i > 300:
        time.sleep(0.1)
        print('sleep')'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Vertical_Print_Sideways~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for i in range (0,360):
    if i % 3 == 0:
        print("")
        for x in range (i,,)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Diagonal_Print_Sideways_Test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''for rows in range(6):
    colour_wall[colour+1 + rows*60] =(255,255,255)
    colour = colour + 1
    client.put_pixels(colour_wall)


for rows in range (6):
    colour_wall[colour-1 + rows*60] =(255,255,255)
    colour = colour - 1
    client.put_pixels(colour_wall)
    '''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Diagonal_Print_2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Hourglass_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
inc = 0
loop = 0
'''
for i in range(3):
    for i in range(10,51):
        print("i = ", i)
        colour[i] =(255,255,255)
        client.put_pixels(colour)
        client.put_pixels(colour)
        time.sleep(0.1)
        colour[i] =(0,0,0)
        client.put_pixels(colour)
        client.put_pixels(colour)
        #vert print code here
        for x in range(i):
            x = i + 60
            print("x = ",x)
            colour[x] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            time.sleep(0.05)
            colour[x] =(0,0,0)
            client.put_pixels(colour)
            client.put_pixels(colour)
            if x == x: 
                break
    if i == 50:
        for x in range(50,10,-1):
            print ("x = ", x)
            colour[x] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            time.sleep(0.1)
            #vert print code here 
            time.sleep(0.1)
            colour[x] =(0,0,0)
            client.put_pixels(colour)
            client.put_pixels(colour)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Flags_Dribble_Line_print~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
inc = 0
loop = 0

for i in range(3):
    for i in range(10,51):
        print(i)
        #turn led on
        colour[i] =(255,255,255)
        client.put_pixels(colour)
        client.put_pixels(colour)
        #turn led off i-1
        colour[i-1] =(0,0,0)
        client.put_pixels(colour)
        client.put_pixels(colour)
        time.sleep(0.1)
        for x in range(i+60):
            x = i + 60*inc
            colour[x] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            if x == x:
                break
        print("x =",x)
    inc = inc + 1
    print ("inc =",inc)
    if i == 50:
        for i in range (50,9,-1):
            print (i)
            #print reverse down
            colour[i] =(255,255,255)
            client.put_pixels(colour)
            client.put_pixels(colour)
            time.sleep(0.1)
            if inc < 5:    
                #turn off previous led 
                colour[i] =(0,0,0)
                client.put_pixels(colour)
                client.put_pixels(colour)
                #time.sleep(0.1)
                # i +1
            for x in range(i):
                x = i + 60*inc
                colour[x] =(255,255,255)
                client.put_pixels(colour)
                client.put_pixels(colour)
                print("x = ", x)
                if x == x:
                    break
                #time.sleep(0.1)
        inc = inc + 1
        print ("inc =",inc)
    if i == 10 or i == 50:
        loop = loop +1
        print ("loop = ",loop)
        # increment 6 times 
        ##need to add vertical print 
        #downwards with deletion occruring in line with inrement number
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Hourglass~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
