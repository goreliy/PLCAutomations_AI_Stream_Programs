import json
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime

# Функция, которая обновляет значения переменных и обновляет их на ползунках
def update_variables():
    try:
        # Чтение данных из файла JSON
        with open('values.json') as json_file:
            data = json.load(json_file)
        
        # Обновление значений переменных
        for slider_name in sliders:
            sliders[slider_name].set(data[slider_name])
            
            # Добавление значения переменной в историю с меткой времени
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history[slider_name].append((data[slider_name], timestamp))

        # Обновление графика
        update_graph()
        
        # Сохранение данных в архивный файл JSON
        with open('arch.json', 'w') as arch_file:
            json.dump(history, arch_file)
    except FileNotFoundError:
        print("Файл не найден")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
    except IOError:
        print("Ошибка ввода-вывода при чтении файла")

    # Запланировать обновление переменных через 1 секунду
    root.after(1000, update_variables)

# Функция, которая обновляет график
def update_graph(event=None):
    plt.clf()  # Очистить предыдущий график
    
    # Добавить график для каждой переменной
    for slider_name in history:
        values, timestamps = zip(*history[slider_name])  # Разделить значения и метки времени
        plt.plot(timestamps, values, label=slider_name)  # Использовать метки времени на оси X
    
    # Настроить оси и легенду
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.legend()
    
    # Поворот меток времени на оси X для лучшей читаемости
    plt.xticks(rotation=45, ha='right')
    
    # Обновить график в окне tkinter
    canvas.draw()

# Создание окна приложения
root = tk.Tk()
root.title('JSON данные')

# Регистрация функции обновления графика для события <Configure> (изменение размеров окна)
root.bind('<Configure>', update_graph)

# Создание слайдеров и переменных для значений
sliders = {}
variables = {}
history = {}

try:
    # Чтение данных из файла JSON
    with open('values.json') as json_file:
        data = json.load(json_file)
        
        for slider_name in data:
            # Создание переменной для значения слайдера
            variables[slider_name] = tk.IntVar()
            variables[slider_name].set(data[slider_name])
            
            # Создание слайдера
            slider = ttk.Scale(root, from_=0, to=100, variable=variables[slider_name])
            slider.pack()
            
            # Сохранение слайдера в словаре по имени
            sliders[slider_name] = slider
            
            # Создание истории значения переменной
            history[slider_name] = []
except FileNotFoundError:
    print("Файл не найден")
except json.JSONDecodeError:
    print("Ошибка декодирования JSON")
except IOError:
    print("Ошибка ввода-вывода при чтении файла")

# Создание графического окна для графика
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Заполнение окна

# Задержка обновления графика для избежания чрезмерного обновления
canvas.draw()
fig.tight_layout()

# Запуск функции обновления переменных
update_variables()

# Запуск главного цикла окна приложения
root.mainloop()