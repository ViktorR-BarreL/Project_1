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
        screenshot = ImageGrab.grab(bbox=(round(w * .0141), round(h * .0277), round(w * .488), round(h * .972)))
        screenshot.save(filepath)


# Функция для включения и выключения музыки
def toggle_music(button1, img_off, img_on):
    if music_playing.get():
        winsound.PlaySound(None, winsound.SND_PURGE)  # Остановить воспроизведение
        music_playing.set(False)
        button1.configure(image=img_off)
    else:
        winsound.PlaySound("source/music2.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        music_playing.set(True)
        button1.configure(image=img_on)


def menu_on_screen():
    label = Label(menu, image=bg)
    label.place(relx=.5, rely=.5, anchor='center')

    label1 = Label(bg='#96b3cf', image=name)
    label1.place(relx=.5, rely=.31, anchor='center')

    button1 = tk.Button(command=menu.destroy, image=ex, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    button1.place(relx=.54, rely=.86, anchor="center", relwidth=.07, relheight=.129)

    b_play = tk.Button(image=play, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf', command=game)
    b_play.place(relx=.5, rely=.71, anchor="center", relwidth=.245, relheight=.13)

    music_button = Button(command=lambda: toggle_music(music_button, sound_off, sound_on), borderwidth=0, bg='#96b3cf',
                          activebackground='#96b3cf')
    music_button.place(relx=.46, rely=.86, anchor='center', relwidth=.07, relheight=.129)

    if not music_playing.get():
        music_button.configure(image=sound_off)
    else:
        music_button.configure(image=sound_on)


def game():
    forget_menu()
    bmen = tk.Button(command=cheta, image=ex_menu, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    bmen.place(relx=.961, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    save_bt = tk.Button(command=save_screenshot, image=save, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    save_bt.place(relx=.909, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    label_bar_cat = Label(bg='#96b3cf', image=bar_cat)
    label_bar_cat.place(relx=.747, rely=.158, anchor='center')

    label_bar_col = Label(bg='#96b3cf', image=bar_col)
    label_bar_col.place(relx=.956, rely=.597, anchor='center')

    label_bg_menu = Label(bg='#96b3cf', image=bg_menu)
    label_bg_menu.place(relx=.718, rely=.598, anchor='center')

    label_bg_charat = Label(bg='#96b3cf', image=so_so)
    label_bg_charat.place(relx=.251, rely=.5, anchor='center')

    music1 = Button(command=lambda: toggle_music(music1, sound_off1, sound_on1), borderwidth=0, bg='#96b3cf',
                    activebackground='#96b3cf')
    music1.place(relx=.857, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    if not music_playing.get():
        music1.configure(image=sound_off1)
    else:
        music1.configure(image=sound_on1)

    body_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=body_img)
    body_bt.place(relx=.539, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    features_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=features_img)
    features_bt.place(relx=.585, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    eyes_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=eyes_img)
    eyes_bt.place(relx=.632, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    hair_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=hair_img)
    hair_bt.place(relx=.678, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    top_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=top_img)
    top_bt.place(relx=.724, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    bottom_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=bottom_img)
    bottom_bt.place(relx=.771, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    socks_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=socks_img)
    socks_bt.place(relx=.817, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    shoes_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=shoes_img)
    shoes_bt.place(relx=.864, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    glasses_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=glasses_img)
    glasses_bt.place(relx=.9099, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    acc_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=acc_img)
    acc_bt.place(relx=.956, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    color1_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color1)
    color1_bt.place(relx=0.956, rely=.278, anchor='center', relwidth=.04167, relheight=.0741)

    color2_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color2)
    color2_bt.place(relx=0.956, rely=.356, anchor='center', relwidth=.04167, relheight=.0741)

    color3_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color3)
    color3_bt.place(relx=0.956, rely=.435, anchor='center', relwidth=.04167, relheight=.0741)

    color4_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color4)
    color4_bt.place(relx=0.956, rely=.514, anchor='center', relwidth=.04167, relheight=.0741)

    color5_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color5)
    color5_bt.place(relx=0.956, rely=.593, anchor='center', relwidth=.04167, relheight=.0741)

    color6_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color6)
    color6_bt.place(relx=0.956, rely=.671, anchor='center', relwidth=.04167, relheight=.0741)

    color7_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color7)
    color7_bt.place(relx=0.956, rely=.75, anchor='center', relwidth=.04167, relheight=.0741)

    color8_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color8)
    color8_bt.place(relx=0.956, rely=.829, anchor='center', relwidth=.04167, relheight=.0741)

    color9_bt = tk.Button(borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=color9)
    color9_bt.place(relx=0.956, rely=.909, anchor='center', relwidth=.04167, relheight=.0741)

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


body_img = Image.open('source/body.png')
body_img = body_img.resize((round(w * (body_img.width/1920)), round(h * (body_img.height / 1080))))
body_img = ImageTk.PhotoImage(body_img)

features_img = Image.open('source/features.png')
features_img = features_img.resize((round(w * (features_img.width/1920)),
                                    round(h * (features_img.height / 1080))))
features_img = ImageTk.PhotoImage(features_img)

eyes_img = Image.open('source/eye.png')
eyes_img = eyes_img.resize((round(w * (eyes_img.width/1920)), round(h * (eyes_img.height / 1080))))
eyes_img = ImageTk.PhotoImage(eyes_img)

hair_img = Image.open('source/hair.png')
hair_img = hair_img.resize((round(w * (hair_img.width/1920)), round(h * (hair_img.height / 1080))))
hair_img = ImageTk.PhotoImage(hair_img)

top_img = Image.open('source/upp.png')
top_img = top_img.resize((round(w * (top_img.width/1920)), round(h * (top_img.height / 1080))))
top_img = ImageTk.PhotoImage(top_img)

bottom_img = Image.open('source/downn.png')
bottom_img = bottom_img.resize((round(w * (bottom_img.width/1920)),
                                round(h * (bottom_img.height / 1080))))
bottom_img = ImageTk.PhotoImage(bottom_img)

socks_img = Image.open('source/socks.png')
socks_img = socks_img.resize((round(w * (socks_img.width/1920)), round(h * (socks_img.height / 1080))))
socks_img = ImageTk.PhotoImage(socks_img)

shoes_img = Image.open('source/shoes.png')
shoes_img = shoes_img.resize((round(w * (shoes_img.width/1920)), round(h * (shoes_img.height / 1080))))
shoes_img = ImageTk.PhotoImage(shoes_img)

glasses_img = Image.open('source/glasses.png')
glasses_img = glasses_img.resize((round(w * (glasses_img.width/1920)), round(h * (glasses_img.height / 1080))))
glasses_img = ImageTk.PhotoImage(glasses_img)

acc_img = Image.open('source/accs.png')
acc_img = acc_img.resize((round(w * (acc_img.width/1920)), round(h * (acc_img.height / 1080))))
acc_img = ImageTk.PhotoImage(acc_img)

color1 = Image.open('source/color1.png')
color1 = color1.resize((round(w * .04167), round(h * .0741)))
color1 = ImageTk.PhotoImage(color1)

color2 = Image.open('source/color2.png')
color2 = color2.resize((round(w * .04167), round(h * .0741)))
color2 = ImageTk.PhotoImage(color2)

color3 = Image.open('source/color3.png')
color3 = color3.resize((round(w * .04167), round(h * .0741)))
color3 = ImageTk.PhotoImage(color3)

color4 = Image.open('source/color4.png')
color4 = color4.resize((round(w * .04167), round(h * .0741)))
color4 = ImageTk.PhotoImage(color4)

color5 = Image.open('source/color5.png')
color5 = color5.resize((round(w * .04167), round(h * .0741)))
color5 = ImageTk.PhotoImage(color5)

color6 = Image.open('source/color6.png')
color6 = color6.resize((round(w * .04167), round(h * .0741)))
color6 = ImageTk.PhotoImage(color6)

color7 = Image.open('source/color7.png')
color7 = color7.resize((round(w * .04167), round(h * .0741)))
color7 = ImageTk.PhotoImage(color7)

color8 = Image.open('source/color8.png')
color8 = color8.resize((round(w * .04167), round(h * .0741)))
color8 = ImageTk.PhotoImage(color8)

color9 = Image.open('source/color9.png')
color9 = color9.resize((round(w * .04167), round(h * .0741)))
color9 = ImageTk.PhotoImage(color9)

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

# Изображение включения/выключения музыки
sound_on = Image.open('source/sound_on.png')
sound_on = sound_on.resize((round(w * .068), round(h * .121)))
sound_on = ImageTk.PhotoImage(sound_on)

sound_off = Image.open('source/sound_off.png')
sound_off = sound_off.resize((round(w * .068), round(h * .121)))
sound_off = ImageTk.PhotoImage(sound_off)

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

# Переменная для отслеживания состояния музыки
music_playing = BooleanVar()
winsound.PlaySound('source/music2.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)  # Включить музыку
music_playing.set(True)

menu_on_screen()

menu.mainloop()

# Beach by Sakura Girl | https://soundcloud.com/sakuragirl_official
# Music promoted by https://www.chosic.com/free-music/all/
# Creative Commons CC BY 3.0
# https://creativecommons.org/licenses/by/3.0/
