from tkinter import *  # Імпортуємо всі елементи з модуля tkinter, щоб створити графічний інтерфейс користувача
import random  # Імпортуємо модуль random для генерації випадкових значень
import time  # Імпортуємо модуль time для створення затримок у виконанні програми

# Клас для створення кульки в грі
class Ball:
    # Ініціалізатор класу
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas  # Отримуємо полотно, на якому буде рухатися кулька
        self.paddle = paddle  # Встановлюємо об'єкт ракетки
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # Малюємо кульку на полотні
        self.canvas.move(self.id, 245, 100)  # Початкове розміщення кульки на полотні
        starts = [-3, -2, -1, 1, 2, 3]  # Створюємо можливі напрямки для старту кульки
        random.shuffle(starts)  # Перемішуємо список для випадкового вибору напрямку
        self.x = starts[0]  # Присвоюємо випадковий горизонтальний напрямок
        self.y = -3  # Початковий вертикальний напрямок
        self.canvas_height = self.canvas.winfo_height()  # Отримуємо висоту полотна
        self.canvas_width = self.canvas.winfo_width()  # Отримуємо ширину полотна
        self.hit_bottom = False  # Позначаємо, що кулька ще не досягла дна

    # Функція для перевірки, чи вдарила кулька ракетку
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)  # Отримуємо координати ракетки
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # Перевірка на горизонтальне зіткнення
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:  # Перевірка на вертикальне зіткнення
                return True  # Повертаємо True, якщо є зіткнення
        return False  # Повертаємо False, якщо зіткнення немає

    # Функція для переміщення кульки
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # Переміщуємо кульку на полотні
        pos = self.canvas.coords(self.id)  # Отримуємо нові координати кульки
        if pos[1] <= 0:  # Якщо кулька досягла верхньої межі полотна
            self.y = 3  # Змінюємо напрямок руху на вниз
        if pos[3] >= self.canvas_height:  # Якщо кулька досягла дна
            self.hit_bottom = True  # Позначаємо, що кулька вдарилася об дно
        if self.hit_paddle(pos):  # Якщо кулька вдарила ракетку
            self.y = -3  # Змінюємо напрямок на вгору
        if pos[0] <= 0:  # Якщо кулька вдарила ліву межу полотна
            self.x = 3  # Змінюємо напрямок на вправо
        if pos[2] >= self.canvas_width:  # Якщо кулька вдарила праву межу полотна
            self.x = -3  # Змінюємо напрямок на вліво

# Клас для створення ракетки
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas  # Отримуємо полотно
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # Малюємо ракетку на полотні
        self.canvas.move(self.id, 200, 300)  # Початкове розміщення ракетки
        self.x = 0  # Початковий горизонтальний напрямок ракетки
        self.canvas_width = self.canvas.winfo_width()  # Отримуємо ширину полотна
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)  # Зв'язуємо клавішу вліво з функцією turn_left
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)  # Зв'язуємо клавішу вправо з функцією turn_right

    # Функція для переміщення ракетки
    def draw(self):
        self.canvas.move(self.id, self.x, 0)  # Переміщуємо ракетку по горизонталі
        pos = self.canvas.coords(self.id)  # Отримуємо координати ракетки
        if pos[0] <= 0:  # Якщо ракетка досягла лівої межі полотна
            self.x = 0  # Зупиняємо рух ліворуч
        elif pos[2] >= self.canvas_width:  # Якщо ракетка досягла правої межі полотна
            self.x = 0  # Зупиняємо рух вправо

    # Функція для повороту ракетки вліво
    def turn_left(self, evt):
        self.x = -2  # Встановлюємо рух вліво

    # Функція для повороту ракетки вправо
    def turn_right(self, evt):
        self.x = 2  # Встановлюємо рух вправо

# Створення основного вікна гри
tk = Tk()
tk.title("Games")  # Назва вікна
tk.resizable(0, 0)  # Заборона зміни розміру вікна
tk.wm_attributes("-topmost", 1)  # Встановлюємо вікно на передній план

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # Створюємо полотно з певними параметрами
canvas.pack()  # Додаємо полотно у вікно

tk.update()  # Оновлюємо вікно, щоб отримати розміри

paddle = Paddle(canvas, 'blue')  # Створюємо об'єкт ракетки
ball = Ball(canvas, paddle, 'red')  # Створюємо об'єкт кульки

# Основний цикл гри
while not ball.hit_bottom:  # Поки кулька не досягла дна
    ball.draw()  # Викликаємо метод draw для кульки
    paddle.draw()  # Викликаємо метод draw для ракетки
    tk.update_idletasks()  # Оновлюємо завдання інтерфейсу
    tk.update()  # Оновлюємо вікно
    time.sleep(0.01)  # Додаємо затримку для плавності анімації

tk.mainloop()  # Запускаємо головний цикл програми
