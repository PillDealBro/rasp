#import sys
import time
import RPi.GPIO as GPIO

# note to myself ---> OBRATI PAZNJU NA RAZMAKE

GPIO.setmode(GPIO.BCM) #gledaju se GPIO brojevi 

#definisani pinovi (GPIO)
Triger = 23
Eko = 24
led_crvena = 18
led_zelena = 25
led_zuta = 8
led_zuta1 = 7
#---------------

#definisanje pinova INPUT ili OUTPUT
GPIO.setup(Triger, GPIO.OUT)
GPIO.setup(Eko, GPIO.IN)
GPIO.setup(led_crvena, GPIO.OUT)
GPIO.setup(led_zelena,GPIO.OUT)
GPIO.setup(led_zuta,GPIO.OUT)
GPIO.setup(led_zuta1,GPIO.OUT)
GPIO.output(led_crvena,False)
GPIO.output(led_zelena,False)
GPIO.output(led_zuta,False)
GPIO.output(led_zuta1,False)

#--------------------------------

#funkcija za razdaljinu
def razdaljina():

    GPIO.output(Triger,True)
    #0.01ms
    time.sleep(0.00001)
    GPIO.output(Triger,False)
    
    #kada je Eko pin primio signal logicke 1? 
    PulsPocetak = time.time()
    PulsPrimljen = time.time()

    while GPIO.input(Eko) == 0:
        PulsPocetak = time.time()
    while GPIO.input(Eko) == 1:
        PulsPrimljen = time.time()

    #razlika u vremenu od 0 (dok je ECHO pin LOW) do 1 (dok je ECHO pin HIGH) da bi dobili koliko je zapravo trajao puls
    trajanje_pulsa = PulsPrimljen - PulsPocetak
    razdaljina = (trajanje_pulsa * 34300) / 2

    return razdaljina
#-----------------------------------------

if __name__ == '__main__':
    try:
     while True:

         #test program
         
         razda = razdaljina()
        
             
         print ("%.1f cm" %razda)
         time.sleep(0.3)
 
         #---------------------------

    #Nastavak zadatka ...
         
         if(razda<20):
             GPIO.output(led_crvena,True)
             GPIO.output(led_zuta,False)
             GPIO.output(led_zuta1,False)
             GPIO.output(led_zelena,False)
             time.sleep(0.3)
         if(razda<18):
             
             GPIO.output(led_crvena,False)
             GPIO.output(led_zuta,True)
             GPIO.output(led_zuta1,False)
             GPIO.output(led_zelena,False)
             time.sleep(0.3)
         if(razda>22):
             GPIO.output(led_crvena,False)
             GPIO.output(led_zuta1,True)
             GPIO.output(led_zuta,False)
             GPIO.output(led_zelena,False)
             time.sleep(0.3)
         if(razda >=18 and razda<=22):
             GPIO.output(led_crvena,False)
             GPIO.output(led_zuta,False)
             GPIO.output(led_zuta1,False)
             GPIO.output(led_zelena,True)
             time.sleep(0.3)


    #----------------------------
    
    #Prekinemo pomocu CTRL + C     
    except KeyboardInterrupt:
        print("Merenje zaustavljeno")
        GPIO.cleanup()
