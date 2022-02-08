import opc
import time

colour=[(0,0,0)]*360

client = opc.Client('localhost:7890')

for i in range (300,360):
    print ("i",i)
    colour[i] =(0,255,255)
    client.put_pixels(colour)
    if i % 2 != 0:
        for x in range(i,i-360,-60):
            print("x",x)
            colour[x] =(0,255,255)
            client.put_pixels(colour)
            time.sleep(0.06)
    else:
        for x in range(i,i-360,-60):
            print("x",x)
            colour[x] =(0,255,0)
            client.put_pixels(colour)
            time.sleep(0.06)
       # time.sleep(0.1)

for i in range(0,30):
    print("i",i)
    colour[i] = (0,0,0)
    colour[i+60] = (0,0,0)
    colour[i+120] = (0,0,0)
    client.put_pixels(colour)
    time.sleep(0.05)
    
for i in range(359,330,-1):
    print("i",i)
    colour[i] = (0,0,0)
    colour[i-60] = (0,0,0)
    colour[i-120] = (0,0,0)
    client.put_pixels(colour)
    time.sleep(0.05)
    
for i in range(180,210):
    print("i",i)
    colour[i] = (0,0,0)
    colour[i+60] = (0,0,0)
    colour[i+120] = (0,0,0)
    client.put_pixels(colour)
    time.sleep(0.05)

for i in range(60,30,-1):
    print("i",i)
    colour[i] = (0,0,0)
    colour[i+60] = (0,0,0)
    colour[i+120] = (0,0,0)
    client.put_pixels(colour)
    time.sleep(0.05)

for i in range (143,158):
    print(i)
    colour[i] =(0,255,0)
    client.put_pixels(colour)
    time.sleep(0.05)

for i in range(360):
    if i % 2 == 0:
        print ("i",i)
        colour[i] =(0,255,0)
        colour[i+1] =(0,255,0)
        client.put_pixels(colour)
        time.sleep(0.05)
    
        if i % 4 == 0:
            print ("i",i)
            colour[i] =(0,0,0)
            colour[i+1] =(0,0,0)
            client.put_pixels(colour)
            time.sleep(0.05)

for i in range(360):
    print("i",i)
    colour[i] =(0,0,0)
    client.put_pixels(colour)
    if  i == 59 or i == 119 or i == 179 or i == 239 or i == 299:
        print("i",i)
        time.sleep(0.5)