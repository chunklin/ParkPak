import serial
from firebase import firebase
firebase = firebase.FirebaseApplication('https://parkpak-c41e3.firebaseio.com/')
ard = serial.Serial('/dev/tty96B0', 115200)

while 1:
    ardOut = ard.readline()
    print(ardOut)
    
    #string format: XX.XX|XX.XX|XX.XX|XXX|XXX|XX.XX\r\n'
    #               012345678901234567890123456789012 3 4
    
    temp = ardOut[0:5]
    humidity = ardOut[6:11]
    light = ardOut[18:21]
    sound = ardOut[22:25]
    print(sound)
    UV = ardOut[26:30]
    soil = ardOut[31:35]
    print(UV)
    result = firebase.put(
        '',
        '/user',
        {
            "UV": UV.decode('utf-8'),
            "humidity": humidity.decode('utf-8'),
            "lightlevel": light.decode('utf-8'),
            "soilmoisture": soil.decode('utf-8'),
            "sound": sound.decode('utf-8'),
            "temperature": temp.decode('utf-8')
        }
    ) 

