from tkinter import *
import tkinter as tk
import ctypes
import winsound
import pyscreenshot as ImageGrab
from tkinter import filedialog
from PIL import Image, ImageTk

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def forget_screen():
    for widget in screen.winfo_children():
        widget.destroy()


def reset_game():
    global image_objects, images
    image_objects = {}
    images = {}


def draw_layers():
    global canvas1
    canvas1.delete("all")  # очищаем холст перед отрисовкой слоев
    for layer_number in range(0, 14):  # отрисовываем слои в порядке 1, 2,...13
        layer = f"layer{layer_number}"
        if layer in image_objects:
            canvas1.create_image((w * 0.242), (h * 0.5), image=images[layer], anchor='center')


def add_layer(layer_number, image_path):
    global canvas1
    image = process_image(image_path)  # используем функцию process_image для обработки изображения
    images[f"layer{layer_number}"] = image
    if f"layer{layer_number}" in image_objects:
        canvas1.delete(image_objects[f"layer{layer_number}"])
    image_objects[f"layer{layer_number}"] = canvas1.create_image((w * 0.242), (h * 0.5),
                                                                 image=images[f"layer{layer_number}"], anchor='center')
    draw_layers()


def delete_colors():
    global colors
    for color in colors:
        color.destroy()
    colors.clear()


def color_on_scr(cc):
    global colors
    delete_colors()

    for i in range(cc):
        # Загрузка изображения для кнопки
        image = process_image(f'source/etc/color{i}.png')
        # Создание кнопок
        color = tk.Button(command=lambda j=i: (selected_j.set(j), body()), borderwidth=0, bg='#de6e82',
                          activebackground='#de6e82', image=image)
        color.place(relx=0.956, rely=.278 + i * .0796, anchor='center', relwidth=.04167, relheight=.0741)
        color.image = image  # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
        colors.append(color)


# Списки для хранения количества цветов по каждой категории
other = [9, 9, 9, 9, 9, 9, 9, 9, 9]
feat_c = [1, 5, 1, 8]
up_c = [9, 5, 9, 9, 2, 9, 9, 9, 9]
down_c = [8, 8, 8, 9, 9, 8, 8]
socks_c = [2, 5, 4, 4]
shoes_c = [9, 7, 5, 5, 9, 9, 5, 7, 9]
glass_c = [2, 2]
acs_c = [3, 5, 4, 3, 4, 3]
eye_c = [9, 9, 1]


def create_buttons(bt_count, list_c):
    global buttons
    for button in buttons:
        button.destroy()
    buttons.clear()

    # Расстояние между кнопками
    x_padding = 16
    y_padding = 13

    buttons = []
    i = selected_i.get()
    k = selected_k.get()
    for n in range(bt_count):  # Создаем кнопки
        # Загрузка изображения для кнопки
        cc = list_c[n]
        image = process_image(f'source/{i}/{k}/slots/{n}.png')
        button = tk.Button(image=image, command=lambda s=n, z=cc: (selected_n.set(s), selected_j.set(0),
                           color_on_scr(z), body()), bg='#de6e82', activebackground='#de6e82', borderwidth=0)
        button.image = image  # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
        button.place(x=(w * .586) + (n % 3) * (w * .124 + w * 0.0083),
                     y=(h * .366) + (n // 3) * (h * .220 + h * 0.01204), anchor='center')
        buttons.append(button)


def hair_buttons():
    global buttons
    for button in buttons:
        button.destroy()
    buttons.clear()

    # Расстояние между кнопками
    x_padding = 0.0083 // w
    y_padding = 0.01204 // h

    buttons = []
    i = selected_i.get()
    k = selected_k.get()
    for n in range(9):  # Создаем кнопки
        # Загрузка изображения для кнопки
        image = process_image(f'source/{i}/{k}/slots/{n}.png')
        # Если это третья кнопка, удаляем 0-й и 6-й слои и добавляем 7-й слой
        if n == 2:
            button = tk.Button(image=image, command=lambda s=n: (selected_n.set(s), image_objects.pop("layer0", None),
                               image_objects.pop("layer6", None), selected_layer.set(7), body(), color_on_scr(9)),
                               bg='#de6e82', activebackground='#de6e82', borderwidth=0)
        else:
            layer_num = 6 if n < 3 else 0
            # Если это кнопка с номером 1 или 2, добавляем 6-й слой
            # Если это кнопка с номером 4-9, удаляем 7-й слой и добавляем 0-й слой
            if n < 2:
                button = tk.Button(image=image, command=lambda s=n, layer=layer_num: (selected_n.set(s), image_objects.pop("layer7", None),
                                   selected_layer.set(layer), body(), color_on_scr(9)), bg='#de6e82',
                                   activebackground='#de6e82', borderwidth=0)
            else:
                button = tk.Button(image=image, command=lambda s=n, layer=layer_num: (selected_n.set(s),
                                   image_objects.pop("layer7", None), selected_layer.set(layer), body(),
                                   color_on_scr(9)), bg='#de6e82', activebackground='#de6e82', borderwidth=0)
        button.image = image  # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
        button.place(x=w * .586 + (n % 3) * (w * .124 + w * 0.0083),
                     y=h * .366 + (n // 3) * (h * .220 + h * 0.01204), anchor='center')
        buttons.append(button)


def body():
    j = selected_j.get()
    i = selected_i.get()
    k = selected_k.get()
    n = selected_n.get()
    layer_num = selected_layer.get()
    add_layer(layer_num, f'source/{i}/{k}/{n}/{j}.png')


def save_screenshot():
    # Запрашиваем у пользователя путь для сохранения
    filepath = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

    # Если пользователь выбрал путь, сохраняем скриншот
    if filepath:
        screenshot = ImageGrab.grab(bbox=(round(w * .0094), round(h * .0185), round(w * .494), round(h * .981)))
        screenshot.save(filepath)


# Функция для включения и выключения музыки
def toggle_music(button1, img_off, img_on):
    if music_playing.get():
        winsound.PlaySound(None, winsound.SND_PURGE)  # Остановить воспроизведение
        music_playing.set(False)
        button1.configure(image=img_off)
    else:
        winsound.PlaySound("source/etc/music2.wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        music_playing.set(True)
        button1.configure(image=img_on)


def choice_of_type():
    forget_screen()
    doll1_bt = tk.Button(command=lambda i='Doll1': (selected_i.set(i), game()), borderwidth=0, bg='#96b3cf',
                         activebackground='#96b3cf', image=slot)
    doll2_bt = tk.Button(command=lambda i='Doll2': (selected_i.set(i), game()), borderwidth=0, bg='#96b3cf',
                         activebackground='#96b3cf', image=slot)
    doll1_bt.place(relx=.719, rely=.5, anchor='center')
    doll2_bt.place(relx=.281, rely=.5, anchor='center')


def menu_on_screen():
    forget_screen()
    label = Label(screen, image=bg)
    label.place(relx=.5, rely=.5, anchor='center')

    label1 = Label(bg='#96b3cf', image=name)
    label1.place(relx=.5, rely=.31, anchor='center')

    button1 = tk.Button(command=screen.destroy, image=ex, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
    button1.place(relx=.54, rely=.86, anchor="center", relwidth=.07, relheight=.129)

    b_play = tk.Button(image=play, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf', command=choice_of_type)
    b_play.place(relx=.5, rely=.71, anchor="center", relwidth=.245, relheight=.13)

    music_button = tk.Button(command=lambda: toggle_music(music_button, sound_off, sound_on), borderwidth=0,
                             bg='#96b3cf', activebackground='#96b3cf')
    music_button.place(relx=.46, rely=.86, anchor='center', relwidth=.07, relheight=.129)

    if not music_playing.get():
        music_button.configure(image=sound_off)
    else:
        music_button.configure(image=sound_on)


# словарь для хранения изображений
images = {}

# список для отслеживания порядка слоев
layers = []

# словарь для хранения объектов изображений на холсте
image_objects = {}


def delete_layer(layer_num):
    global image_objects
    # Удалить слой из image_objects и canvas1
    if f"layer{layer_num}" in image_objects:
        canvas1.delete(image_objects[f"layer{layer_num}"])
        del image_objects[f"layer{layer_num}"]
    # Перерисовать оставшиеся слои
    draw_layers()


def bye_bye(ki, lay):
    global del_bt
    del_bt.destroy()

    del_bt = tk.Button(command=lambda l1=lay: delete_layer(l1), borderwidth=0, bg='#de6e82', activebackground='#de6e82',
                       image=delete_lay_img)
    del_bt.place(relx=.539 + ki * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)


def bye_bye_hairs(ki):
    global del_bt
    del_bt.destroy()

    del_bt = tk.Button(command=lambda: (delete_layer(0), delete_layer(6), delete_layer(7)), borderwidth=0, bg='#de6e82',
                       activebackground='#de6e82', image=delete_lay_img)
    del_bt.place(relx=.539 + ki * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)


def game():
    global canvas1, del_bt
    reset_game()
    forget_screen()
    bmen = tk.Button(command=menu_on_screen, image=ex_menu, borderwidth=0, bg='#96b3cf', activebackground='#96b3cf')
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

    canvas1 = tk.Canvas(width=w * .484, height=h * .963)
    canvas1.place(relx=.251, rely=.5, anchor='center')

    i2 = selected_i.get()
    add_layer(4, f'source/{i2}/0/контур.png')
    add_layer(3, f'source/{i2}/0/тень.png')
    add_layer(1, f'source/{i2}/0/0/0.png')
    add_layer(5, f'source/{i2}/2/0/0.png')

    music_button2 = Button(command=lambda: toggle_music(music_button2, sound_off1, sound_on1), borderwidth=0,
                           bg='#96b3cf', activebackground='#96b3cf')
    music_button2.place(relx=.857, rely=.0556, anchor='center', relwidth=.0469, relheight=0.0833)

    if not music_playing.get():
        music_button2.configure(image=sound_off1)
    else:
        music_button2.configure(image=sound_on1)

    body_bt = tk.Button(command=lambda layer_num=1, k=0: (del_bt.destroy(), selected_layer.set(layer_num),
                        selected_k.set(k), delete_colors(), create_buttons(1, other)),borderwidth=0,
                        bg='#de6e82', activebackground='#de6e82', image=body_img)
    body_bt.place(relx=.539 + 0 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    features_bt = tk.Button(command=lambda layer_num=2, k=1, j=0: (bye_bye(1, 2), selected_layer.set(layer_num),
                            selected_k.set(k), delete_colors(), create_buttons(4, feat_c)), borderwidth=0,
                            bg='#de6e82', activebackground='#de6e82', image=features_img)
    features_bt.place(relx=.539 + 1 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    eyes_bt = tk.Button(command=lambda layer_num=5, k=2: (del_bt.destroy(), selected_layer.set(layer_num),
                        selected_k.set(k), delete_colors(), create_buttons(3, eye_c)), borderwidth=0,
                        bg='#de6e82', activebackground='#de6e82', image=eyes_img)
    eyes_bt.place(relx=.539 + 2 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    hair_bt = tk.Button(command=lambda layer_num=6, k=3, j=0: (bye_bye_hairs(3), selected_layer.set(layer_num),
                        selected_k.set(k), delete_colors(), selected_j.set(j), hair_buttons()),
                        borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=hair_img)
    hair_bt.place(relx=.539 + 3 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    top_bt = tk.Button(command=lambda layer_num=11, k=4: (bye_bye(4, 11), selected_layer.set(layer_num),
                       selected_k.set(k), delete_colors(), create_buttons(9, up_c)),
                       borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=top_img)
    top_bt.place(relx=.539 + 4 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    bottom_bt = tk.Button(command=lambda layer_num=10, k=5: (bye_bye(5, 10), selected_layer.set(layer_num),
                          selected_k.set(k), delete_colors(), create_buttons(7, down_c)),
                          borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=bottom_img)
    bottom_bt.place(relx=.539 + 5 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    socks_bt = tk.Button(command=lambda layer_num=8, k=6: (bye_bye(6, 8), selected_layer.set(layer_num),
                         selected_k.set(k), delete_colors(), create_buttons(4, socks_c)),
                         borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=socks_img)
    socks_bt.place(relx=.539 + 6 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    shoes_bt = tk.Button(command=lambda layer_num=9, k=7: (bye_bye(7, 9), selected_layer.set(layer_num),
                         selected_k.set(k), delete_colors(), create_buttons(9, shoes_c)),
                         borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=shoes_img)
    shoes_bt.place(relx=.539 + 7 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    glasses_bt = tk.Button(command=lambda layer_num=12, k=8: (bye_bye(8, 12), selected_layer.set(layer_num),
                           selected_k.set(k), delete_colors(), create_buttons(2, glass_c)),
                           borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=glasses_img)
    glasses_bt.place(relx=.539 + 8 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)

    acc_bt = tk.Button(command=lambda layer_num=13, k=9: (bye_bye(9, 13), selected_layer.set(layer_num),
                       selected_k.set(k), delete_colors(), create_buttons(6, acs_c)),
                       borderwidth=0, bg='#de6e82', activebackground='#de6e82', image=acc_img)
    acc_bt.place(relx=.539 + 9 * .0464, rely=.158, anchor='center', relwidth=.04167, relheight=.0741)


# Настройка основного окна
screen = Tk()
screen.iconbitmap('source/etc/icon.ico')

w = screen.winfo_screenwidth()
h = screen.winfo_screenheight()

screen.attributes('-fullscreen', True)
screen.configure(bg='#96b3cf')


def process_image(path):
    img = Image.open(path)
    img = img.resize((round(w * (img.width / 1920)), round(h * (img.height / 1080))))
    img = ImageTk.PhotoImage(img)
    return img


bg = process_image('source/etc/bg.png')

# Категории выбора
body_img = process_image('source/etc/body.png')
features_img = process_image('source/etc/features.png')
eyes_img = process_image('source/etc/eye.png')
hair_img = process_image('source/etc/hair.png')
top_img = process_image('source/etc/upp.png')
bottom_img = process_image('source/etc/downn.png')
socks_img = process_image('source/etc/socks.png')
shoes_img = process_image('source/etc/shoes.png')
glasses_img = process_image('source/etc/glasses.png')
acc_img = process_image('source/etc/accs.png')

delete_lay_img = process_image('source/etc/delete.png')

# Название Игры
name = process_image('source/etc/GameName.png')

# Изображение для начала игры
play = process_image('source/etc/play.png')

# Изображение выхода из игры
ex = process_image('source/etc/exit.png')

# Изображения включения/выключения музыки
sound_on = process_image('source/etc/sound_on.png')
sound_off = process_image('source/etc/sound_off.png')

# Элементы игрового окна

# Выход в меню
ex_menu = process_image('source/etc/exmenu.png')

# Музыка
sound_on1 = process_image('source/etc/sound_onn.png')
sound_off1 = process_image('source/etc/sound_offf.png')

# Рамка для предметов
bg_menu = process_image('source/etc/bgmenu.png')

# Рамка для категорий
bar_cat = process_image('source/etc/barcat.png')

# Рамка для цветов
bar_col = process_image('source/etc/barcol.png')

# Рамка для фона персонажа
so_so = process_image('source/etc/so.png')

# Кнопка сохранения
save = process_image('source/etc/save.png')

# Штуки для одевалки
slot = process_image('source/etc/main_slot.png')
slot_bt = process_image('source/etc/slot.png')

# Переменная для отслеживания состояния музыки
music_playing = BooleanVar()
winsound.PlaySound('source/etc/music2.wav',
                   winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)  # Включить музыку
music_playing.set(True)

canvas1 = tk.Canvas()
del_bt = tk.Button()

selected_j = tk.IntVar()
selected_j.set(0)
selected_n = tk.IntVar()
selected_n.set(0)
selected_i = tk.StringVar()
selected_i.set('Doll1')
selected_k = tk.IntVar()
selected_k.set(0)
selected_layer = tk.IntVar()
selected_layer.set(0)

buttons = []
colors = []

menu_on_screen()

screen.mainloop()
