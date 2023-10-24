def konversi(j=0):
    def menit(m=0):
        def detik (d=0):
            return ((j*60)+m)*60+d
        return detik
    return menit

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

is_integer = lambda s: s.isdigit()

output = []

for item in data:
    components = item.split()  
    integers = list(filter(is_integer, components))  
    integers = [int(i) for i in integers]  
    output.append(integers)

print(output)



