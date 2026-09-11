distance = float(input("Введите расстояние (км):"))
speed = float(input("Введите скорость (км/ч):"))
fuel_rashod = float(input("Введите расход топлива (л/100 км):"))
time = distance / speed
total_fuel = (distance / 100) * fuel_rashod
print(f"Маршрут: {distance} км, скорость {speed} км/ч")
print(f"Время в пути: {time:.2f} часов")
print(f"Расход топлива: {fuel_rashod} л/100 км")
print(f"Общий расход: {total_fuel:.2f} литров")