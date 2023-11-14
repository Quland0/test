
import math

def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def find_triangle_type(a, b, c):
    if a == b and b == c:
        return "Равносторонний треугольник"
    elif a == b or b == c or a == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

def find_triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(area, 2)

def main():
    try:
        a = float(input("Введите длину первой стороны треугольника: "))
        b = float(input("Введите длину второй стороны треугольника: "))
        c = float(input("Введите длину третьей стороны треугольника: "))

        if check_triangle(a, b, c):
            print("Треугольник существует")
            print("Вид треугольника:", find_triangle_type(a, b, c))
            print("Площадь треугольника:", find_triangle_area(a, b, c))
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
                return "некорректный тип данных"
        else:
            print("Треугольник не существует")
    except ValueError:
        print("некорректный тип данных")

if __name__ == "__main__":
    main()
