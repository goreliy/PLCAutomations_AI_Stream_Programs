from pymodbus.client.sync import ModbusSerialClient
import json
import time

def main():
    # Настройки COM порта
    port = "COM4"
    baudrate = 115200
    parity = 'N'
    stopbits = 1
    bytesize = 8
    timeout = 1

    # Создание Modbus клиента
    client = ModbusSerialClient(method='rtu')
    client.port = port
    client.baudrate = baudrate
    client.parity = parity
    client.stopbits = stopbits
    client.bytesize = bytesize
    client.timeout = timeout

    # Настройки файла
    filename = "values.json"

    try:
        # Открытие соединения с устройством
        if not client.connect():
            print("Не удалось установить соединение с устройством!")
            return

        while True:
            # Чтение регистра 8202
            result = client.read_input_registers(address=8202, count=1, unit=16)

            if result.isError():
                print(f"Ошибка чтения регистра: {result}")
            else:
                value = result.registers[0] / 100.0
                print(f"Register 8202: {value}")

                # Запись значения в файл
                data = {}
                try:
                    with open(filename, 'r') as file:
                        data = json.load(file)
                except FileNotFoundError:
                    pass

                data['slider1'] = value

                try:
                    with open(filename, 'w') as file:
                        json.dump(data, file)
                except IOError:
                    print(f"Ошибка записи в файл {filename}")

            # Задержка между чтениями 0.5 секунды
            time.sleep(0.5)

    except Exception as e:
        print(f"Возникла ошибка: {e}")
    finally:
        # Закрытие соединения
        client.close()

if __name__ == '__main__':
    main()