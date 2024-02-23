import tkinter as tk
import pyscreenshot as ImageGrab
from tkinter import filedialog

# Функция для сохранения скриншота
def save_screenshot():
    # Запрашиваем у пользователя путь для сохранения
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

    # Если пользователь выбрал путь, сохраняем скриншот
    if filepath:
        screenshot = ImageGrab.grab(bbox=(0, 0, 100, 100))
        screenshot.save(filepath)

# Создаем окно
root = tk.Tk()
root.title("Скриншот программы")

# Создаем кнопку "Сохранить"
save_button = tk.Button(root, text="Сохранить", command=save_screenshot)
save_button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()