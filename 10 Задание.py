
seconds1 = int(input("Введите количество секунд с момента старта:"))
hours = seconds1 // 3600
minutes = (seconds1 % 3600) // 60
seconds2 = seconds1 % 60
print(f"Время с момента старта: {seconds1} секунд.")
print(f"Форматированное время: {hours} ч {minutes} мин {seconds2} сек.")