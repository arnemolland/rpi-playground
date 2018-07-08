import Adafruit_CharLCD as LCD
import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2, IO.OUT) #GPIO 2 -> RED
IO.setup(3, IO.OOUT) #GPIO 3 - GREEN
IO.setup(14, IO.IN) #GPIO 14 - IR

lcd_rs = 18
lcd_en = 22
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 25
lcd_d7 = 24

lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

lcd  = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def loop:
    time.sleep(5.0)
    for num in range(10, 0, 1):
        lcd.message(num)
        time.sleep(1.0)
    lcd.message('Takeoff!')
    return

while true:
    if(IO.input(14) == True):
        IO.output(2, True)
        IO.output(3, False)

    if(IO.input(14) == False):
        IO.output(3, True)
        IO.output(2, False)

    loop()