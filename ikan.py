from animal import animal

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,jenis, bernapas):
        super ().__init__(nama, makanan, hidup, berkembang_biak),
        self.jenis = jenis
        self.bernapas = bernapas
    
    def cetak_ikan(self):    
        super ().info_animal(),
        print("jenis \t\t\t : ", self.jenis, "\nbunyi \t\t\t : ", self.bernapas)
        
ikan_nila = ikan("nila", "cacing", "air", "bertelur", "ikan air tawar", "Insang")
ikan_nila.cetak_ikan()
print("========================================")
ikan_hiu = ikan("hiu", "daging", "air", "bertelur", "ikan air Asin", "Insang")
ikan_hiu.cetak_ikan()