import math

#x = A, m, sy = 2
#y = B, tx =  2
#z = B, ty, sx = 8


def apply_transformations(func):
    def decorator(x, y, z):
        def translasi(tx, ty):
            return func(x, y + tx, z + ty)

        def rotasi(sudut_rotasi):
            radians = math.radians(sudut_rotasi)
            x_new = x * math.cos(radians) - y * math.sin(radians)
            y_new = x * math.sin(radians) + y * math.cos(radians)
            return func(x_new, y_new, z)

        def perbesaran(skala):
            return func(x * skala, y * skala, z * skala)    

        def garis_transformasi(m, b, sy):
            return lambda x: m * x + b + sy

        return translasi, rotasi, perbesaran, garis_transformasi

    return decorator

@apply_transformations
def hasil_transformasi(x, y, z):
    return x, y, z

x_input = float(input("Masukkan nilai x: "))
y_input = float(input("Masukkan nilai y: "))
z_input = float(input("Masukkan nilai z: "))

translasi, rotasi, perbesaran, garis_transformasi = hasil_transformasi(x_input, y_input, z_input)

tx_input = float(input("Masukkan nilai tx untuk translasi: "))
ty_input = float(input("Masukkan nilai ty untuk translasi: "))
sudut_rotasi_input = float(input("Masukkan nilai sudut rotasi untuk rotasi (dalam derajat): "))
skala_input = float(input("Masukkan nilai skala untuk perbesaran: "))
m_input = float(input("Masukkan nilai m untuk persamaan garis: "))
b_input = float(input("Masukkan nilai b untuk persamaan garis: "))
sy_input = float(input("Masukkan nilai sy untuk persamaan garis: "))

hasil_translasi = translasi(tx_input, ty_input)
hasil_rotasi = rotasi(sudut_rotasi_input)
hasil_perbesaran = perbesaran(skala_input)

print("\nHasil Translasi:", hasil_translasi)
print("Hasil Rotasi:", hasil_rotasi)
print("Hasil Perbesaran:", hasil_perbesaran)

print("\nHasil Garis Transformasi:")
for x_value in range(0, 10):
    hasil_garis = garis_transformasi(m_input, b_input, sy_input)(x_value)
    print(f"For x = {x_value}, y = {hasil_garis:.2f}")

contoh_garis = f"y = {m_input:.2f}x + {b_input:.2f} + {sy_input:.2f}"
print(f"\nContoh persamaan garis transformasi: {contoh_garis}")
