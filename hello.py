
import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_stars_and_suraj(rows=20, columns=40, star_density=0.1):
    suraj = [
        "  *****   **    *****   **    **  ",
        " **      *  *   *      *  *  *  * ",
        "  *****  ****   *****  ****  **** ",
        "      ** *  *       ** *  *  *  * ",
        "  *****  *  *   *****  *  *  *  * "
    ]
    
    # Simulate stars dropping
    for _ in range(rows):
        clear_screen()
        for _ in range(rows):
            line = ''.join('*' if random.random() < star_density else ' ' for _ in range(columns))
            print(line)
        time.sleep(0.1)
    
    # Display "SURAJ" at the bottom
    clear_screen()
    for line in suraj:
        print(line)
        time.sleep(0.2)

def main():
    print("Simulating stars dropping and displaying 'SURAJ':\n")
    print_stars_and_suraj()

if __name__ == "__main__":
    main()

