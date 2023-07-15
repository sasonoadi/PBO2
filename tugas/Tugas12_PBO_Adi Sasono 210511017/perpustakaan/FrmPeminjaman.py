import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1200x1200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='CODE_PINJAM:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_KEMBALI:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BATAS_TGL_KEMBALI:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DENDA_PER_HARI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUMLAH_HARI:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TOTAL_DENDA:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_PETUGAS:').grid(row=8, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtCode_pinjam = Entry(mainFrame) 
        self.txtCode_pinjam.grid(row=0, column=1, padx=5, pady=5)
        self.txtCode_pinjam.bind("<Return>", self.onCari)
        self.txtTanggal_kembali = Entry(mainFrame) 
        self.txtTanggal_kembali.grid(row=1, column=1, padx=5, pady=5)
        self.txtBatas_tgl_kembali = Entry(mainFrame) 
        self.txtBatas_tgl_kembali.grid(row=2, column=1, padx=5, pady=5)
        self.txtDenda_per_hari = Entry(mainFrame) 
        self.txtDenda_per_hari.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtJumlah_hari = Entry(mainFrame) 
        self.txtJumlah_hari.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtTotal_denda = Entry(mainFrame) 
        self.txtTotal_denda.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=6, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame) 
        self.txtKode_buku.grid(row=7, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_petugas = Entry(mainFrame) 
        self.txtKode_petugas.grid(row=8, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('kode_kembali','code_pinjam','tanggal_kembali','batas_tgl_kembali','denda_per_hari','jumlah_hari','total_denda','kode_anggota','kode_buku','kode_petugas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kode_kembali', text='KODE_KEMBALI')
        self.tree.column('kode_kembali', width="100")
        self.tree.heading('code_pinjam', text='CODE_PINJAM')
        self.tree.column('code_pinjam', width="100")
        self.tree.heading('tanggal_kembali', text='TANGGAL_KEMBALI')
        self.tree.column('tanggal_kembali', width="150")
        self.tree.heading('batas_tgl_kembali', text='BATAS_TGL_KEMBALI')
        self.tree.column('batas_tgl_kembali', width="150")
        self.tree.heading('denda_per_hari', text='DENDA_PER_HARI')
        self.tree.column('denda_per_hari', width="150")
        self.tree.heading('jumlah_hari', text='JUMLAH_HARI')
        self.tree.column('jumlah_hari', width="100")
        self.tree.heading('total_denda', text='TOTAL_DENDA')
        self.tree.column('total_denda', width="100")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="100")
        self.tree.heading('kode_petugas', text='KODE_PETUGAS')
        self.tree.column('kode_petugas', width="100")
        # set tree position
        self.tree.place(x=0, y=350)
        
    def onClear(self, event=None):
        self.txtCode_pinjam.delete(0,END)
        self.txtCode_pinjam.insert(END,"")
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,"")
        self.txtBatas_tgl_kembali.delete(0,END)
        self.txtBatas_tgl_kembali.insert(END,"")
        self.txtDenda_per_hari.delete(0,END)
        self.txtDenda_per_hari.insert(END,"")
        self.txtJumlah_hari.delete(0,END)
        self.txtJumlah_hari.insert(END,"")
        self.txtTotal_denda.delete(0,END)
        self.txtTotal_denda.insert(END,"")
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kode_kembali"],d["code_pinjam"],d["tanggal_kembali"],d["batas_tgl_kembali"],d["denda_per_hari"],d["jumlah_hari"],d["total_denda"],d["kode_anggota"],d["kode_buku"],d["kode_petugas"]))
    def onCari(self, event=None):
        code_pinjam = self.txtCode_pinjam.get()
        obj = Peminjaman()
        a = obj.get_by_code_pinjam(code_pinjam)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        code_pinjam = self.txtCode_pinjam.get()
        obj = Peminjaman()
        res = obj.get_by_code_pinjam(code_pinjam)
        self.txtTanggal_kembali.delete(0,END)
        self.txtTanggal_kembali.insert(END,obj.tanggal_kembali)
        self.txtBatas_tgl_kembali.delete(0,END)
        self.txtBatas_tgl_kembali.insert(END,obj.batas_tgl_kembali)
        self.txtDenda_per_hari.delete(0,END)
        self.txtDenda_per_hari.insert(END,obj.denda_per_hari)
        self.txtJumlah_hari.delete(0,END)
        self.txtJumlah_hari.insert(END,obj.jumlah_hari)
        self.txtTotal_denda.delete(0,END)
        self.txtTotal_denda.insert(END,obj.total_denda)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,obj.kode_buku)
        self.txtKode_petugas.delete(0,END)
        self.txtKode_petugas.insert(END,obj.kode_petugas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        code_pinjam = self.txtCode_pinjam.get()
        tanggal_kembali = self.txtTanggal_kembali.get()
        batas_tgl_kembali = self.txtBatas_tgl_kembali.get()
        denda_per_hari = self.txtDenda_per_hari.get()
        jumlah_hari = self.txtJumlah_hari.get()
        total_denda = self.txtTotal_denda.get()
        kode_anggota = self.txtKode_anggota.get()
        kode_buku = self.txtKode_buku.get()
        kode_petugas = self.txtKode_petugas.get()
        # create new Object
        obj = Peminjaman()
        obj.code_pinjam = code_pinjam
        obj.tanggal_kembali = tanggal_kembali
        obj.batas_tgl_kembali = batas_tgl_kembali
        obj.denda_per_hari = denda_per_hari
        obj.jumlah_hari = jumlah_hari
        obj.total_denda = total_denda
        obj.kode_anggota = kode_anggota
        obj.kode_buku = kode_buku
        obj.kode_petugas = kode_petugas
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_code_pinjam(code_pinjam)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        code_pinjam = self.txtCode_pinjam.get()
        obj = Peminjaman()
        obj.code_pinjam = code_pinjam
        if(self.ditemukan==True):
            res = obj.delete_by_code_pinjam(code_pinjam)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()