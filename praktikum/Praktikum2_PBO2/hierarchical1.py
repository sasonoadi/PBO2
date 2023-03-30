class BPJS_Ketenagakerjaan:
    def __init__(self, nomor_akun, saldo_JHT, saldo_JP):
        self.nomor_akun = nomor_akun 
        self.saldo_JHT = saldo_JHT
        self.saldo_JP = saldo_JP
    def get_nomor_akun(self): return self.nomor_akun
    def get_saldo_JHT(self): return self.saldo_JHT
    def get_saldo_JP(self):
        return self.saldo_JP
    
class Akun_BPJS_Ketenagakerjaan(BPJS_Ketenagakerjaan):
    def __init__(self, nomor_akun, saldo_JHT, saldo_JP , persentase_bunga_deposito):
        super().__init__(nomor_akun, saldo_JHT, saldo_JP) 
        self.persentase_bunga_deposito = persentase_bunga_deposito
    def get_persentase_bunga_deposito(self): return self.persentase_bunga_deposito

class CekAkunBPJS(BPJS_Ketenagakerjaan):
    def __init__(self, nomor_akun, saldo_JHT, saldo_JP, ajukan_klaim):
        super().__init__(nomor_akun, saldo_JHT, saldo_JP) 
        self.ajukan_klaim = ajukan_klaim
    def get_ajukan_klaim(self): return self.ajukan_klaim

# Hierarchical Inheritance
class JointAccount(Akun_BPJS_Ketenagakerjaan):
    def __init__(self, nomor_akun, saldo_JHT, saldo_JP, persentase_bunga_deposito, pemilik_akun):
        super().__init__(nomor_akun, saldo_JHT, saldo_JP , persentase_bunga_deposito) 
        self.pemilik_akun = pemilik_akun
    def get_pemilik_akun(self):
        return self.pemilik_akun
    
jointAccoun = JointAccount('160202','Rp.200jt','Rp.500jt','20%','Adi Sasono')
print('Nomor Akun       : ',jointAccoun.get_nomor_akun())
print('Saldo JHT        : ',jointAccoun.get_saldo_JHT())
print('Saldo JP         : ',jointAccoun.get_saldo_JP())
print('Presentase Bunga : ',jointAccoun.get_persentase_bunga_deposito())
print('Owners           : ',jointAccoun.get_pemilik_akun())
