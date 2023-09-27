import json
import time

# Функция для чтения значений из файла values.json
def read_values_from_file():
    try:
        with open('values.json') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл values.json не найден")
        return None
    except json.JSONDecodeError:
        print("Неверный формат файла values.json")
        return None

# Функция для записи значения в файл values.json
def write_value_to_file(value):
    try:
        with open('values.json', 'r+') as file:
            data = json.load(file)
            data['slider5'] = value
            file.seek(0)
            json.dump(data, file)
            file.truncate()
    except FileNotFoundError:
        print("Файл values.json не найден")
    except json.JSONDecodeError:
        print("Неверный формат файла values.json")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Константы для настройки PID-регулятора
Kp = float(input("Введите значение Kp: "))
Ki = float(input("Введите значение Ki: "))
Kd = float(input("Введите значение Kd: "))

# Функция для расчета выходного воздействия PID-регулятора
def calculate_control_output(slider1, slider2, last_error, integral):
    setpoint = slider1
    measured_value = slider2
    
    error = setpoint - measured_value
    derivative = error - last_error
    
    integral += error
    control_output = Kp * error + Ki * integral + Kd * derivative
    
    return control_output, error, integral

if __name__ == '__main__':
    integral = 0
    last_error = 0
    
    while True:
        data = read_values_from_file()
        if data is None:
            time.sleep(1)
            continue
        
        slider1 = data.get('slider1', 0)
        slider2 = data.get('slider2', 0)
        
        control_output, last_error, integral = calculate_control_output(slider1, slider2, last_error, integral)
        print(f"Выходное воздействие PID-регулятора: {control_output}")
        
        write_value_to_file(control_output)
        
        time.sleep(0.5)