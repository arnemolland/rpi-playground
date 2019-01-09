import Adafruit_CharLCD as LCD
import RPi.GPIO as IO
import time

def countdown():
    i = 10
    while i >= 0:
        lcd.message(str(i))
        time.sleep(1.0)
        lcd.clear()
        if i == 0:
            lcd.message('Takeoff!')

        i = i-1

    time.sleep(2.0)
    lcd.clear()
    return

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2, IO.OUT) #GPIO 2 -> RED
IO.setup(3, IO.OUT) #GPIO 3 - GREEN
IO.setup(14, IO.IN) #GPIO 14 - IR

lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18

lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

lcd  = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

while True:
    if(IO.input(14) == True):
        IO.output(2, True)
        IO.output(3, False)

    if(IO.input(14) == False):
        IO.output(3, True)
        IO.output(2, False)

    countdown()