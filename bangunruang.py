import math

def l_balok(p, L ,t):
    hitung =2 *( p * L )+ (p * t) + (L * t)
    print(f'Luas Balok Adalah {hitung}')

def l_kubus(pl, pt ,lt):
    hitung =2 *( pl + pt + lt )
    print(f'Luas kubus Adalah {hitung}')

def l_tabung(r2, t):
    hitung =6 *(r2 + t )
    print(f'Luas tabung Adalah {hitung}')

def l_prisma(alas, t):
    hitung = 1/2 *(alas + t )
    print(f'Luas prisma Adalah {hitung}')

def l_limas(alas, st):
    hitung = math.sqrt(3) *alas + st  
    print(f'Luas limas Adalah {hitung}')

