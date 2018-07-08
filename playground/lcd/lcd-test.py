import Adafruit_CharLCD as LCD
import time

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

lcd.message('Hallo paa do')

time.sleep(5.0)

for x in range(2, 30):
    lcd.message(x)