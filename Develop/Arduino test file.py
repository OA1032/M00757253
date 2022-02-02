import serial  # if missing in the command prompt or terminal  python-pip install pyserial
## Arduino code(Serial.available() > 0) {
# incomingByte = Serial.read()
# if incomingByte is string;
#       display string on LCD somehow
# }
# 
arduino = serial.Serial('COM3',9600)
time.sleep(2)

#exaple for multiple input
# pot1,pot2, ldr = int(data.split(',')) # "255,204,0" = ["255","204","0"] = [255,204,0]

while True:
    data = int(arduino.readline().decode('utf-8'))# work for default println behaviour. use str() if you are sending large datasets
    print(data)

    # within the folder, puthon filename.py


def send_to_arduino(data):
    arduino.write(str(data).encode('bytes'))
