from pynput.mouse import Button, Controller
import keyboard
import time



mouse = Controller()

while True:

    
    if keyboard.read_key() == "n":
        
            while True:          
     
                    time.sleep(0.01)

                    mouse.press(Button.right) 

                    mouse.release(Button.right)

                    if keyboard.is_pressed('n'): 
                        break


                

                
   



    if keyboard.read_key() == "v":
        
            while True:          
     
                    time.sleep(0.01)

                    mouse.press(Button.left) 

                    mouse.release(Button.left)

                    if keyboard.is_pressed('v'): 
                        break

        
    
    
   
       
         
                
 
     
