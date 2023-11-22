def perkalian(a):
    def dengan(b):
        return a*b
    return dengan 

#hof
variabel_kali = perkalian(6)
hasil = variabel_kali(10)
print("hasil pake hof: ")
print(hasil)

#currying
times = perkalian(5)(7)
print("hasil pake currying: ")
print(times)

