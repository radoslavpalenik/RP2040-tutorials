import neopixel
import machine
import time

pin = machine.Pin(16, machine.Pin.OUT) #LED pin on board (16 for RP2040 Zero)
led = neopixel.NeoPixel(pin, 1) #(pin, number of LEDs)

#To change LED behavior, change these parameters
steps = 30
step_size = 8
step_speed = 0.06


#Cycling colors
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
purple = (128,0,128)

rainbow = [red, yellow, green, blue, purple]


#Changes LED values by increments of 1 defined step
def change_color(target_color, direction):
    #Gets current LED values
    r,g,b = led.__getitem__(0)
    
    #Sets new value to the LED if not meeting required color yet (for each RGB component)
    if(r != target_color[0]):
        if r + step_size * direction != target_color[0]:
            r = r + step_size * direction
        else:
            r = target_color[0]
                
    if(g != target_color[1]):
                
        if g + step_size * direction != target_color[1]:
            g = g + step_size * direction
        else:
            g = target_color[1]
                    
    if(b != target_color[2]):
        if b + step_size * direction != target_color[2]:
            b = b + step_size * direction
        else:
            b = target_color[2]
            
    return (r,g,b)
    
#Direction determines if LED is lightening(1) or darkening(-1)
def lighten_led(color, direction):

    #Gradually lightens/darkens LED 
    for i in range(steps):
     
        new_color = change_color(color, direction)
        led.fill(new_color)
        led.write()
        time.sleep(step_speed)

        #Dont perform upcoming steps if target color reached
        if new_color[0] == color[0] and new_color[1] == color[1] and new_color[2] == color[2]:
            break
        
#Immitates breathing by lightening and darkening LED
def led_breathe(color):
     lighten_led(color,1)
     time.sleep(0.2)
     lighten_led(black,-1)
     time.sleep(0.2)
               

# Loop to make LED breathe
while True:
    for rain_col in rainbow:
        led_breathe(rain_col)
    