## Program Title: Modbus RTU Register Scanner

**Description:**
Modbus RTU Register Scanner is a console application designed for searching readable registers of Modbus RTU devices. The program allows for configuring Modbus parameters, setting search ranges, and saving search results in JSON format.

## Functional Requirements:

1. **Modbus Parameter Configuration:**
   - Baud rate (bits/sec)
   - Parity (odd, even, none)
   - Stop bits (1, 2)
   - Device address (0 to 255)
   - Port number (1 to 65535)
   - Timeout in milliseconds (100 to 10000)

2. **Setting Search Ranges:**
   - Starting register (0 to 65535)
   - Ending register (0 to 65535)

3. **Stopping and Resuming Search.** When the search is stopped, the program saves the current search state and can resume it later.

4. **Saving search results in JSON format.** For each found register, the following data is saved:
   - Device address
   - Register number
   - Register value
   - Query execution time

5. **Inputting search parameters through the console** during program startup or using saved settings from separate files.

6. **Validation of entered Modbus parameters and device address.** Checking the correctness of the device address within the range of 0 to 255.

7. **Indication of waiting time and execution progress** using a progress bar.

8. **Displaying registers and their values in decimal and hexadecimal formats.**

9. **Handling errors** when reading registers or receiving no response from Modbus devices. The program should continue to the next registers without interrupting the search.

## File Structure:

1. Configuration file with program settings. File format - JSON.
2. Files with saved settings. File format - JSON.

**Initial Configuration Files:**
1. config.json - file with program settings.
2. settings.json - file with saved settings.

> Note: The program should implement the logic of working with Modbus RTU devices and use standard libraries for working with JSON, console input-output, and progress bars.





Название программы: Modbus RTU Register Scanner

# Описание:
Программа Modbus RTU Register Scanner представляет собой консольное приложение, предназначенное для поиска доступных для чтения регистров устройств Modbus RTU. Программа позволяет настраивать параметры Modbus, задавать диапазоны поиска и сохранять результаты поиска в формате JSON.

# Функциональные требования:
## 1. Настройка параметров Modbus:
   - Скорость передачи данных (бит/сек)
   - Четность (нечетная, четная, нет)
   - Стопбиты (1, 2)
   - Адрес прибора (от 0 до 255)
   - Номер порта (от 1 до 65535)
   - Таймаут в миллисекундах (от 100 до 10000)

## 2. Задание диапазонов поиска:
   - Начальный регистр (от 0 до 65535)
   - Конечный регистр (от 0 до 65535)

## 3. Остановка и продолжение поиска. При остановке поиска программа сохраняет текущее состояние поиска и может продолжить его позже.

## 4. Сохранение результатов поиска в формате JSON. Для каждого найденного регистра сохраняются следующие данные:
   - Адрес устройства
   - Номер регистра
   - Значение регистра
   - Время выполнения запроса

## 5. Ввод параметров поиска через консоль при старте программы или использование сохраненных настроек из отдельных файлов.

## 6. Валидация введенных настроек параметров Modbus и адреса устройства. Проверка корректности адреса устройства в диапазоне от 0 до 255.

## 7. Индикация времени ожидания и прогресса выполнения с помощью прогрессбара.

## 8. Вывод регистров и их значений в формате 10-ричной и 16-ричной систем счисления.

## 9. Обработка ошибок при чтении регистров или отсутствии ответов от устройств Modbus. Программа должна переходить к следующим регистрам, не прерывая поиск.

# Структура файлов:
1. Конфигурационный файл с настройками программы. Формат файла - JSON.
2. Файлы с сохраненными настройками. Формат файла - JSON.

Начальные файлы конфигураций:
1. config.json - файл с настройками программы.
2. settings.json - файл с сохраненными настройками.

Примечание:
Программа должна реализовывать логику работы с устройствами Modbus RTU и использовать стандартные библиотеки для работы с JSON, консольным вводом-выводом и прогрессбарами.
