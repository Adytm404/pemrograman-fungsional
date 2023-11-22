def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_M():
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)

    M = calculate_M()

    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B (berdasarkan soal):")
print(line_equation_of(point(4, -2), point(-1, 3)))
print("Persamaan garis yang melalui titik A dan B (berdasarkan nim):")
print(line_equation_of(point(1, -4), point(-2, 6)))
