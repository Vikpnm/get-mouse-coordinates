import keyboard
import pyautogui

# Функция для записи координат курсора и RGB цвета
def record_mouse_coordinates_and_color(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 's':
        x, y = pyautogui.position()
        color = pyautogui.pixel(x, y)  # Get the RGB color at the cursor's position
        print(f'{x},{y} , RGB Color: {color}')

# Устанавливаем обработчик событий клавиатуры
keyboard.on_press_key('s', record_mouse_coordinates_and_color)

# Ждем, пока пользователь не завершит программу (например, нажмет клавишу Esc)
keyboard.wait('esc')

# Отключаем обработчик событий клавиатуры перед выходом
keyboard.unhook_all()
