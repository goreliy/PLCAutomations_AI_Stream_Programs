## Description

This folder contains the following files:
- data_input.py: a Python file that allows data input using sliders and saves them in JSON format.
- data_output.py: a Python file that displays values as a graph.
- pid_regulation.py: a Python file that implements PID regulation for a single variable. It reads values from a JSON file, performs regulation, and writes the result to another variable in JSON format.
- modbus_polling.py: a Python program that performs polling using the Modbus protocol, reads current values, and writes them to a JSON file for use in PID regulation and graph display.

## Usage

1. Run data_input.py to input data using sliders. Enter the necessary values and save them in a JSON file.
2. Run data_output.py to display the values as a graph. Open the graph to visualize the current data.
3. Run modbus_polling.py to poll the device using the Modbus protocol and write the current values to a JSON file.
4. Run pid_regulation.py to apply PID regulation to a single variable using the values from the JSON file and write the result to another variable in JSON format.

## Dependencies

To run the programs, the following packages need to be installed:
- Python 3.x
- json - built-in module for working with JSON in Python
- matplotlib - library for creating graphs
- pymodbus - library for working with the Modbus protocol

## License

MIT License
## Описание

Это папка содержит следующие файлы:
- data_input.py: файл на языке Python, позволяющий вводить данные с помощью ползунков и сохранять их в формате JSON.
- data_output.py: файл на языке Python, отображающий значения в виде графика.
- pid_regulation.py: файл на языке Python, реализующий PID-регулирование для одной переменной. Он считывает значения из JSON-файла, производит регулирование и записывает результат в другую переменную в формате JSON.
- modbus_polling.py: программа на языке Python, осуществляющая опрос по протоколу Modbus, считывающая текущие значения и записывающая их в JSON-файл для использования в PID-регулировании и отображении графика.

## Использование

1. Запустите data_input.py для ввода данных с помощью ползунков. Введите необходимые значения и сохраните их в JSON-файле.
2. Запустите data_output.py для отображения значений в виде графика. Откройте график для визуализации текущих данных.
3. Запустите modbus_polling.py для опроса устройства по протоколу Modbus и записи текущих значений в JSON-файл.
4. Запустите pid_regulation.py для применения PID-регулирования к одной переменной, используя значения из JSON-файла, и записи результата в другую переменную в формате JSON.

## Зависимости

Для работы программ требуется установка следующих пакетов:
- python версии 3.x
- json - встроенный модуль для работы с JSON в Python
- matplotlib - библиотека для создания графиков
- pymodbus - библиотека для работы с протоколом Modbus

## Лицензия

MIT License
