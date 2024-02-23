from tkinter import *
import tkinter as tk
import ctypes
import winsound
import pyscreenshot as ImageGrab
from tkinter import filedialog
from PIL import Image, ImageTk

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def forget_menu():
    for widget in menu.winfo_children():
        widget.destroy()


def cheta():
    forget_menu()
    menu_on_screen()

def save_screenshot():
    # Запрашиваем у пользователя путь для сохранения
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

    # Если пользователь выбрал путь, сохраняем скриншот
    if filepath:
        screenshot = ImageGrab.grab(bbox=(round(w*.0141), round(h*.0277), round(w*.488), round(h*.972)))
        screenshot.save(filepath)

def menu_on_screen():
    label = Label(menu, image=bg)
    label.place(relx=.5, rely=.5, anchor='center')

    label1 = Label(bg='#96b3cf', image=name)
    label1.place(relx=.5, rely=.31, anchor='center')

    button1 = tk.Button(command=menu.destroy, image=ex, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    button1.place(relx=.54, rely=.86, anchor="center", relwidth=.07, relheight=.129)

    b_play = tk.Button(image=play, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf', command=game)
    b_play.place(relx=.5, rely=.71, anchor="center", relwidth=.245, relheight=.13)

    # Функция для включения и выключения музыки
    def toggle_music():
        if music_playing.get():
            winsound.PlaySound(None, winsound.SND_PURGE)  # Остановить воспроизведение
            music_playing.set(False)
            music_button.configure(image=sound_off)
        else:
            winsound.PlaySound("source/music2.wav",
                               winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)  # Включить музыку
            music_playing.set(True)
            music_button.configure(image=sound_on)

    # Создать кнопку для включения/выключения музыки
    sound_on = Image.open('source/sound_on.png')
    sound_on = sound_on.resize((round(w * .068), round(h * .121)))
    sound_on = ImageTk.PhotoImage(sound_on)

    sound_off = Image.open('source/sound_off.png')
    sound_off = sound_off.resize((round(w * .068), round(h * .121)))
    sound_off = ImageTk.PhotoImage(sound_off)

    music_button = Button(menu, command=toggle_music, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf',
                          image=sound_on)
    music_button.place(relx=.46, rely=.86, anchor='center', relwidth=.07, relheight=.129)


def game():
    forget_menu()
    bmen = tk.Button(command=cheta, image=ex_menu, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    bmen.place(relx=.961, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    save_bt = tk.Button(command=save_screenshot, image=save,borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    save_bt.place(relx=.909, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    label_bar_cat = Label(bg='#96b3cf', image=bar_cat)
    label_bar_cat.place(relx=.747, rely=.158, anchor='center')

    label_bar_col = Label(bg='#96b3cf', image=bar_col)
    label_bar_col.place(relx=.956, rely=.597, anchor='center')

    label_bg_menu = Label(bg='#96b3cf', image=bg_menu)
    label_bg_menu.place(relx=.718, rely=.598, anchor='center')

    label_bg_charat = Label(bg='#96b3cf', image=so_so)
    label_bg_charat.place(relx=.251, rely=.5, anchor='center')

    music1 = Button(borderwidth=0, bg='#96b3cf', activebackground='#96b3cf', image=sound_off1)
    music1.place(relx=.857, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)


# Настройка основного окна
menu = Tk()

w = menu.winfo_screenwidth()
h = menu.winfo_screenheight()
print(w, h)

bg = Image.open('source/bg.png')
bg = bg.resize((w, h))
bg = ImageTk.PhotoImage(bg)

menu.attributes('-fullscreen', True)
menu.configure(bg='#96b3cf')

# Название Игры
name = Image.open('source/GameName.png')
name = name.resize((round(w * .448), round(h * .495)))
name = ImageTk.PhotoImage(name)

# Изображение для начала игры
play = Image.open('source/play.png')
play = play.resize((round(w * .24583), round(h * .13056)))
play = ImageTk.PhotoImage(play)

# Изображение выхода из игры
ex = Image.open('source/exit.png')
ex = ex.resize((round(w * .068), round(h * .121)))
ex = ImageTk.PhotoImage(ex)

# Элементы игрового окна

# Выход в меню
ex_menu = Image.open('source/exmenu.png')
ex_menu = ex_menu.resize((round(w * .0469), round(h * .0833)))
ex_menu = ImageTk.PhotoImage(ex_menu)

# Музыка
sound_on1 = Image.open('source/sound_onn.png')
sound_on1 = sound_on1.resize((round(w * .0469), round(h * .0833)))
sound_on1 = ImageTk.PhotoImage(sound_on1)

sound_off1 = Image.open('source/sound_offf.png')
sound_off1 = sound_off1.resize((round(w * .0469), round(h * .0833)))
sound_off1 = ImageTk.PhotoImage(sound_off1)

# Рамка для предметов
bg_menu = Image.open('source/bgmenu.png')
bg_menu = bg_menu.resize((round(w * .416), round(h * .767)))
bg_menu = ImageTk.PhotoImage(bg_menu)

# Рамка для категорий
bar_cat = Image.open('source/barcat.png')
bar_cat = bar_cat.resize((round(w * .4739), round(h * .1019)))
bar_cat = ImageTk.PhotoImage(bar_cat)

# Рамка для цветов
bar_col = Image.open('source/barcol.png')
bar_col = bar_col.resize((round(w * .0573), round(h * .7652)))
bar_col = ImageTk.PhotoImage(bar_col)

# Рамка для фона персонажа
so_so = Image.open('source/so.png')
so_so = so_so.resize((round(w * .484), round(h * .963)))
so_so = ImageTk.PhotoImage(so_so)

save = Image.open('source/save.png')
save = save.resize((round(w * .0469), round(h * .0833)))
save = ImageTk.PhotoImage(save)

menu_on_screen()

# Переменная для отслеживания состояния музыки
music_playing = BooleanVar()
winsound.PlaySound('source/music2.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)  # Включить музыку
music_playing.set(True)

menu.mainloop()

# Beach by Sakura Girl | https://soundcloud.com/sakuragirl_official
# Music promoted by https://www.chosic.com/free-music/all/
# Creative Commons CC BY 3.0
# https://creativecommons.org/licenses/by/3.0/
