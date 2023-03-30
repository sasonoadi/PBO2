class AkunBank:
    def __init__(self, nomor_akun, saldo):
        self.nomor_akun = nomor_akun 
        self.saldo = saldo
    def get_nomor_akun(self): return self.nomor_akun
    def get_saldo(self):
        return self.saldo
    
class AkunTabungan(AkunBank):
    def __init__(self, nomor_akun, saldo, persentase_bunga):
        super().__init__(nomor_akun, saldo) 
        self.persentase_bunga = persentase_bunga
    def get_persentase_bunga(self): return self.persentase_bunga

class CekAkun(AkunBank):
    def __init__(self, nomor_akun, saldo, overdraft_limit):
        super().__init__(nomor_akun, saldo) 
        self.overdraft_limit = overdraft_limit
    def get_overdraft_limit(self): return self.overdraft_limit

# Hierarchical Inheritance
class JointAccount(AkunTabungan):
    def __init__(self, nomor_akun, saldo, persentase_bunga, owners):
        super().__init__(nomor_akun, saldo, persentase_bunga) 
        self.owners = owners
    def get_owners(self):
        return self.owners
    
jointAccoun = JointAccount('160202', '500 miliyar', '10%', 'PT Adi Sukses Makmur')
print('Nomor Akun       : ',jointAccoun.get_nomor_akun())
print('Saldo            : ',jointAccoun.get_saldo())
print('Presentase Bunga : ',jointAccoun.get_persentase_bunga())
print('Owners           : ',jointAccoun.get_owners())
