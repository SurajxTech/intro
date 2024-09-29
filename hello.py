
import os
import random
import time
import threading
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_effect(rows=20, columns=40, drop_speed=0.05, run_time=30, message="@SurajxTech : SURAJ CHAUHAN"):
    start_time = time.time()

    while True:
        # Check if the run time is exceeded
        if time.time() - start_time > run_time:
            break

        clear_screen()
        for _ in range(rows):
            line = ''.join(random.choice(['0', '1', ' ']) for _ in range(columns))
            print(f"\033[32m{line}\033[0m")  # Green color
        time.sleep(drop_speed)

    clear_screen()
    print(f"\033[32m{message}\033[0m")  # Display message in green

def main():
    print("Starting Matrix effect. It will automatically stop and show the message after 30 seconds.\n")
    matrix_effect()

if __name__ == "__main__":
    main()
