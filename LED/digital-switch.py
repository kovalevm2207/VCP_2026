import RPi.GPIO as GPIO
import time                # импортируем модули времени и работы с GPIO

GPIO.setmode(GPIO.BCM)      # задаем режим обращения к портам
led = 26                    # перменная с номером GPIO пина
GPIO.setup(led, GPIO.OUT)   # настраиваем переменную как цифровой выход

button = 13                 # номер GPIO пина кнопки
GPIO.setup(button, GPIO.IN) # настраиваем переменную как цифровой вход

state = 0

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)
        
        while GPIO.input(button):
            time.sleep(0.2) 