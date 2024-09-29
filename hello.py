
import os
import random
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_effect(rows=20, columns=40, drop_speed=0.05, message="SURAJ CHAUHAN PROJECT OWNER"):
    try:
        while True:
            clear_screen()
            for _ in range(rows):
                line = ''.join(random.choice(['0', '1', ' ']) for _ in range(columns))
                print(f"\033[32m{line}\033[0m")  # Green color
            time.sleep(drop_speed)
    except KeyboardInterrupt:
        clear_screen()
        print(f"\033[32m{message}\033[0m")  # Display message in green

def main():
    print("Starting Matrix effect. Press Ctrl+C to stop and see the message.\n")
    matrix_effect()

if __name__ == "__main__":
    main()


