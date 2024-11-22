#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
#print(celcius_ke_fahrenheit(0))    # Output: 32.0
#print(celcius_ke_fahrenheit(100))  # Output: 212.0

def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
print("=============")
print("=============")

#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
#print(is_genap(4))  # Output: True
#print(is_genap(7))  # Output: False

def is_genap(angka):
    return angka % 2 == 0
print(is_genap(2))
print(is_genap(15))
print("======")
print("======")

#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
#nilai (80) #lulus
#nilai(60) #gagal

def keterangan_nilai(nilai):
    print()
    if nilai >= 80 :
        return 'lulus'
    else :
        return 'gagal'
print(keterangan_nilai(90))
print(keterangan_nilai(40))
print("======")
print("======")
#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens bilangan(20) # 1,3,5,7,9,11,13,15,17,19
def bilangan(n):
    for i in range(1, n, 2):
        print(i, end=" ")

bilangan(20)


   


