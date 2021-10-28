import machine
import time
from ws2812b import ws2812b

#Edit the number of LED's according to your strip

num_leds = 60

pixels = ws2812b(num_leds, 0,0)
pixels.brightness(10)
pixels.fill(0, 0, 0)
pixels.show()

print("Start up Sequence")

#Start up Lights

n = 1

while n < num_leds:  
    pixels.set_pixel(n,255,0,0)
    pixels.set_pixel((n-1),0,0,255)
    pixels.show()
    n = n + 1  
    time.sleep (0.1)
 
time.sleep (1)
pixels.fill(0,0,0)

# Set up Temperature Readings

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535


while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
# Edit the '35' below to callibrate your pico - higher or lower as needs be

    tempfloat = 35 - (reading - 0.706)/0.001721
    temp = int(tempfloat)
  
# The following section runs through each pixel, sets colour and on/off by temp

# Temp 0 to 10

    if temp >=  0 and temp <  40:
       pixels.set_pixel(1, 0, 0, 255)
    else:
      pixels.set_pixel(1, 0, 0, 0)
   
    if temp >=  1 and temp <  40:
       pixels.set_pixel(2, 0, 0, 255)
    else:
      pixels.set_pixel(2, 0, 0, 0) 
      
    if temp >=  2 and temp <  40:
       pixels.set_pixel(3, 0, 0, 255)
    else:
      pixels.set_pixel(3, 0, 0, 0) 
      
    if temp >=  3 and temp <  40:
       pixels.set_pixel(4, 0, 0, 255)
    else:
      pixels.set_pixel(4, 0, 0, 0) 
   
    if temp >=  4 and temp <  40:
       pixels.set_pixel(5, 0, 0, 255)
    else:
      pixels.set_pixel(5, 0, 0, 0) 
      
    if temp >=  5 and temp <  40:
       pixels.set_pixel(6, 0, 0, 255)
    else:
      pixels.set_pixel(6, 0, 0, 0) 
      
    if temp >=  6 and temp <  40:
       pixels.set_pixel(7, 0, 0, 255)
    else:
      pixels.set_pixel(7, 0, 0, 0) 
      
    if temp >=  7 and temp <  40:
       pixels.set_pixel(8, 0, 0, 255)
    else:
      pixels.set_pixel(8, 0, 0, 0) 
      
    if temp >=  8 and temp <  40:
       pixels.set_pixel(9, 0, 0, 255)
    else:
      pixels.set_pixel(9, 0, 0, 0) 
      
    if temp >=  9 and temp <  40:
       pixels.set_pixel(10, 0, 0, 255)
    else:
      pixels.set_pixel(10, 0, 0, 0) 
      
# Temp 10 to 15

    if temp >=  10 and temp <  40:
       pixels.set_pixel(11, 0, 255, 0)
    else:
      pixels.set_pixel(11, 0, 0, 0) 
     
     
    if temp >=  11 and temp <  40:
       pixels.set_pixel(12, 0, 255, 0)
    else:
      pixels.set_pixel(12, 0, 0, 0) 
     
     
    if temp >=  12 and temp <  40:
       pixels.set_pixel(13, 0, 255, 0)
    else:
      pixels.set_pixel(13, 0, 0, 0) 
    
    
    if temp >=  13 and temp <  40:
       pixels.set_pixel(14, 0, 255, 0)
    else:
      pixels.set_pixel(14, 0, 0, 0) 
    
    
    if temp >=  14 and temp <  40:
       pixels.set_pixel(15, 0, 255, 0)
    else:
      pixels.set_pixel(15, 0, 0, 0) 
      
#   Temp 15 to 20

    if temp >=  15 and temp <  40:
       pixels.set_pixel(16, 255, 150, 0)
    else:
      pixels.set_pixel(16, 0, 0, 0) 
      
    if temp >=  16 and temp <  40:
       pixels.set_pixel(17, 255, 150, 0)
    else:
      pixels.set_pixel(17, 0, 0, 0) 
     
    if temp >=  16 and temp <  40:
       pixels.set_pixel(17, 255, 150, 0)
    else:
      pixels.set_pixel(17, 0, 0, 0) 
     
    if temp >=  17 and temp <  40:
       pixels.set_pixel(18, 255, 150, 0)
    else:
      pixels.set_pixel(18, 0, 0, 0) 
      
    if temp >=  18 and temp <  40:
       pixels.set_pixel(19, 255, 150, 0)
    else:
      pixels.set_pixel(19, 0, 0, 0)  
      
    if temp >=  19 and temp <  40:
       pixels.set_pixel(20, 255, 150, 0)
    else:
      pixels.set_pixel(20, 0, 0, 0) 

# Temp 20 to 25      
       
    if temp >=  20 and temp <  40:
       pixels.set_pixel(21, 255, 0, 0)
    else:
      pixels.set_pixel(21, 0, 0, 0) 

    if temp >=  21 and temp <  40:
       pixels.set_pixel(22, 255, 0, 0)
    else:
      pixels.set_pixel(22, 0, 0, 0) 
      
    if temp >=  22 and temp <  40:
       pixels.set_pixel(23, 255, 0, 0)
    else:
      pixels.set_pixel(23, 0, 0, 0) 
      
    if temp >=  23 and temp <  40:
       pixels.set_pixel(24, 255, 0, 0)
    else:
      pixels.set_pixel(24, 0, 0, 0) 
      
    if temp >=  24 and temp <  40:
       pixels.set_pixel(25, 255, 0, 0)
    else:
      pixels.set_pixel(25, 0, 0, 0) 
    
    pixels.show()
  
    print (temp)
    time.sleep(2)
    
