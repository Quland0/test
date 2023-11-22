import math

def input_check(side):
    while True:
        try:
            value = float(input(f"Введите длину стороны {side} треугольника: "))
            if value <= 0:
                print("Длина стороны должна быть положительным числом.")
            else:
                return value
        except ValueError:
            print("Некорректный тип данных.")

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"
    else:
        if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
            return "Остроугольный треугольник"
        elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
            return "Тупоугольный треугольник"
        else:
            return "Прямоугольный треугольник"

def calculate_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def main():
    print("Введите длины сторон треугольника:")
    side_a = input_check("A")
    side_b = input_check("B")
    side_c = input_check("C")

    print(triangle_type(side_a, side_b, side_c))
    print(f"Площадь треугольника: {calculate_area(side_a, side_b, side_c)}")

if __name__ == "__main__":
    main()