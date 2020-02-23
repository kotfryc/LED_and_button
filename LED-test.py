import time
import datetime
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # nie chcemy bledow z GPIO
GPIO.setmode(GPIO.BCM)  # numeracja portow GPIO wedlug plytki
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO 16 jako wejscie podciagniete do "gory" 

#definiowanie Ledow
LEDred = 20
LEDYell = 21

# przypisanie GPIO do konkretnych ledow
GPIO.setup(LEDred, GPIO.OUT)   
GPIO.setup(LEDYell, GPIO.OUT) 

# przelaczenie ledow w stan niski przy uruchomieniu
GPIO.output(LEDred, GPIO.LOW)
GPIO.output(LEDYell, GPIO.LOW)

# zmienna okresliajaca stan przycisku:
button = 1

#zmienne czasowa w milisekundach
czas = time.time() *1000 # czas w ktorym przycisk zmienil swoj stan
duration_time1 = 0.0 #jak dlugo przycik pozostaje w konretnym stanie

# jak dlugo trzeba trzymac przycisk wcisniety zeby nastpila zmiana czerownego leda:
pusch_button = 2

try: 
	while True: # poniewaz wejscie przycisku jest podciagniete do gory, 
		# to stan "aktywnym" jest stan niski (przycik nacisniety),
		# wiec trzeba odwrocic wartosci dla zoltej diody:
		
		duration_time1 = time.time() *1000 - czas #obliczamy ile czasu uplunelo od ostatniej zmiany stanu przycisku		
		button = GPIO.input(16)
		time.sleep(0.01) # nie jest konieczne, ale bez tego procesor skoczy na 100% i malina sie zamuli ;) 
		if button ==1:	
			GPIO.output(LEDYell, 0)
			if duration_time1 > pusch_button*1000: # jesli przycisk bedzie odpowiednio dlugo w okreslonym stanie, nastapi zmiana stanu
				GPIO.output(LEDred, 0)
		if button ==0: 
			GPIO.output(LEDYell, 1)
			if duration_time1 > pusch_button*1000:# jesli przycisk bedzie odpowiednio dlugo w okreslonym stanie, nastapi zmiana stanu
				GPIO.output(LEDred, 1)
		if button != GPIO.input(16): # jesli nastapi zmiana stanu przycisku, 
									 #czas w zmiennej bedzie nadpisany na nowo
				czas = time.time() *1000
except KeyboardInterrupt:
		GPIO.cleanup() 
