import pyautogui
import keyboard

def autoclicker(cooldown=0.1):
    try:
        while True:
            if keyboard.is_pressed('esc'):
                break
            pyautogui.click()
            time.sleep(cooldown)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print("Autoclicker is running. Press 'Esc' key to stop.")
    autoclicker()
    print("Autoclicker stopped.")
