def transformasi(tx, ty, sudut_rotasi, sx, sy):
    def translasi(x, y):
        return x + tx, y + ty

    def rotasi(x, y):
        radians = sudut_rotasi * (3.14159 / 180)
        x_baru = x * (sx * sx) + y * sx * sy
        y_baru = x * sy * sx + y * (sy * sy)
        return x_baru, y_baru

    def perbesaran(x, y):
        return x * sx, y * sy

    def transformasi_garis(x1, y1, x2, y2):
        x1, y1 = translasi(x1, y1)
        x2, y2 = translasi(x2, y2)
        x1, y1 = rotasi(x1, y1)
        x2, y2 = rotasi(x2, y2)
        x1, y1 = perbesaran(x1, y1)
        x2, y2 = perbesaran(x2, y2)
        return x1, y1, x2, y2

    return transformasi_garis


def hitung_gradien(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def buat_persamaan_garis(x1, y1, x2, y2):
    gradien = hitung_gradien(x1, y1, x2, y2)
    konstanta = y1 - gradien * x1
    return f"y = {gradien:.2f}x + {konstanta:.2f}"


def main():
    x1, y1 = map(float, input("Masukkan koordinat titik A (format: x y): ").split())
    x2, y2 = map(float, input("Masukkan koordinat titik B (format: x y): ").split())
    tx = float(input("Masukkan translasi tx: "))
    ty = float(input("Masukkan translasi ty: "))
    sudut_rotasi = float(input("Masukkan sudut rotasi (derajat): "))
    sx = float(input("Masukkan faktor skala pada sumbu x: "))
    sy = float(input("Masukkan faktor skala pada sumbu y: "))

    transformasi_garis = transformasi(tx, ty, sudut_rotasi, sx, sy)
    x1_baru, y1_baru, x2_baru, y2_baru = transformasi_garis(x1, y1, x2, y2)

    persamaan_awal = buat_persamaan_garis(x1, y1, x2, y2)
    persamaan_hasil = buat_persamaan_garis(x1_baru, y1_baru, x2_baru, y2_baru)

    print("\nPersamaan garis melalui titik A dan B:")
    print(persamaan_awal)
    print("\nPersamaan garis baru setelah transformasi:")
    print(persamaan_hasil)


if __name__ == "__main__":
    main()
