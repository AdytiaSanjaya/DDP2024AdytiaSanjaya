#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 

#buat minimal 2 objek untuk setiap class childnya

from animal import animal

class burung(animal):
    def __init__(self, nama,makanan,hidup,berkembang_biak,paruh ,warna_bulu):
       super ().__init__(nama,makanan,hidup,berkembang_biak),
       self.paruh = paruh 
       self.warna_bulu = warna_bulu

    def info_burung(self):
        super ().info_animal(),
        print("Paruh \t\t\t :" , self.paruh,
             "\nWarna bulu \t\t :" , self.warna_bulu)
        
burung_beo = burung("Beo","Jagung","Darat","Bertelur","melengkung","warna warni")
burung_beo.info_burung()
print("========================================")
burung_gagak = burung("Gagak","daging","Darat","Bertelur","lurus","hitam")
burung_gagak.info_burung()