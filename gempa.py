class Gempa : 
    lokasi = ''
    skala = ''
    

    # contractor
    def __init__(self, lokasi , skala,):
        self.lokasi = lokasi
        self.skala = skala
        

    #fungsi
    def dampak(self) :
        if self.skala <2 :
            ket = 'Gempa tidak terasa'
        elif self.skala >=2 and self.skala <4 :
            ket = 'bangunan Retak - retak'

        elif self.skala >=4 and self.skala <6 :
            ket = 'bangunan Roboh'

        else :
            ket = 'Bangunan roboh dan berpotensi Tsunami'

        print('Lokasi Gempa', self.lokasi,
              '\nSkala Gempa', self.skala,
              '\nDampak gempa', ket)