print("введите координаты короля")
x_king, y_king = int(input()), int(input())
print("введите координаты фигуры")
x_figura, y_figura = int(input()), int(input())

if abs(x_figura - x_king) == 1 and abs(y_figura - y_king) == 1 or abs(x_figura - x_king) == 0 and abs(
        y_figura - y_king) == 1 or abs(x_figura - x_king) == 1 and abs(y_figura - y_king) == 0:
    print("бьет")
else:
    print("не бьет")