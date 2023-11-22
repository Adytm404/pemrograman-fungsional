def transformasi_translasi(tx, ty):
    def translasi(p):
        x, y = p
        x_bar = x + tx
        y_bar = y + ty
        return x_bar, y_bar
    return translasi  

def transformasi_dilatasi(sx, sy):
    def dilatasi(p):
        x, y = p
        x_bar = x * sx
        y_bar = y * sy
        return x_bar, y_bar
    return dilatasi

import math

def transformasi_rotasi(sudut):
    radian = math.radians(sudut)
    cos_theta = math.cos(radian)
    sin_theta = math.sin(radian)

    def rotasi(p):
        x, y = p
        x_bar = x * cos_theta - y * sin_theta
        y_bar = x * sin_theta + y * cos_theta
        return x_bar, y_bar
    return rotasi

# Titik awal
P = (3, 5)

# Translasi
translasi = transformasi_translasi(2, -1)
P_setelah_translasi = translasi(P)
print("Hasil Translasi:", P_setelah_translasi)

# Dilatasi
dilatasi = transformasi_dilatasi(2, -1)
P_setelah_dilatasi = dilatasi(P)
print("Hasil Dilatasi:", P_setelah_dilatasi)

# Rotasi
rotasi = transformasi_rotasi(30)
P_setelah_rotasi = rotasi(P)
print("Hasil Rotasi:", P_setelah_rotasi)