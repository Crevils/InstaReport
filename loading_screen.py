'''
Don't forget to give credits : D
Author : https://github.com/crevils
Original Repositary : https://github.com/crevils/InstaReport
'''

import time
import sys

def show_loading_screen(t):
    
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r @Crevils/instareport " + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > t:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\r-----------------------------\n\n")