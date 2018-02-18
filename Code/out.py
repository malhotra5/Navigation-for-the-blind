import pyttsx3 as p
import time
engine =p.init()
while True:
    with open("write.txt","r") as f:
        s =  f.read()
    if s == "Done":
        break
    
    engine.say(s)
    engine.runAndWait()
    time.sleep(1)

