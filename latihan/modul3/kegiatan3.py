random_data = [3.1, 2.7, 5, 'Hello', 42, 'Python', 123.45, 'world', 777, 'lany', 732, 45.5]

def cek_tipe(x):
    if isinstance(x, int):
        return 'int'
    elif isinstance(x, float):
        return 'float'
    elif isinstance(x, str):
        return 'string'

def konversi_angka(x):
    if isinstance(x, int):
        ratusan = x // 100
        puluhan = (x % 100) // 10
        satuan = x % 10
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
    else:
        return x

floats = list(filter(lambda x: cek_tipe(x) == 'float', random_data))
ints = list(filter(lambda x: cek_tipe(x) == 'int', random_data))
strings = list(filter(lambda x: cek_tipe(x) == 'string', random_data))

ints_mapped = list(map(konversi_angka, ints))

print("Data Float:", floats)
print("Data Int:", ints_mapped)
print("Data String:", strings)
