import keyboard
import pyautogui

def record_mouse_coordinates_and_color(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 's':
        x, y = pyautogui.position()
        color = pyautogui.pixel(x, y)  # Get the RGB color at the cursor's position
        print(f'{x},{y} , RGB Color: {color}')
keyboard.on_press_key('s', record_mouse_coordinates_and_color)
keyboard.wait('esc')
keyboard.unhook_all()
