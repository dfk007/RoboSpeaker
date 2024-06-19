import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Daud Farzand")
    while True:
        x = input("Enter what you want me to speak ")
        command = f"say {x}"
        os.system(command)

