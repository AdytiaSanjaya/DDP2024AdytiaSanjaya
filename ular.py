from animal import animal

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,jenis, beraktivitas):
        super ().__init__(nama, makanan, hidup, berkembang_biak),
        self.jenis = jenis
        self.beraktivitas = beraktivitas 
    
    def cetak_ular(self):    
        super ().info_animal(),
        print("jenis \t\t\t : ", self.jenis, "\nberaktivitas \t\t : ", self.beraktivitas)
        
ular_kobra = ular("cobra", "ular kecil", "darat", "bertelur", "ular berbisa", "malam")
ular_kobra.cetak_ular()
print("========================================")
ular_anaconda = ular("anaconda", "sapi", "amfibi", "bertelur", "ular raksasa", "siang")
ular_anaconda.cetak_ular()