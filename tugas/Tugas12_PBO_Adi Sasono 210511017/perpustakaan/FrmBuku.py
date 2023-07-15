import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("850x850")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='CODE_BUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN_TERBIT:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STOK_BUKU:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtCode_buku = Entry(mainFrame) 
        self.txtCode_buku.grid(row=0, column=1, padx=5, pady=5)
        self.txtCode_buku.bind("<Return>", self.onCari)
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5)
        self.txtTahun_terbit = Entry(mainFrame) 
        self.txtTahun_terbit.grid(row=4, column=1, padx=5, pady=5)
        self.txtStok_buku = Entry(mainFrame) 
        self.txtStok_buku.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('kode_buku','code_buku','judul','penulis','penerbit','tahun_terbit','stok_buku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="90")
        self.tree.heading('code_buku', text='CODE_BUKU')
        self.tree.column('code_buku', width="90")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="150")
        self.tree.heading('penulis', text='PENULIS')
        self.tree.column('penulis', width="150")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="150")
        self.tree.heading('tahun_terbit', text='TAHUN_TERBIT')
        self.tree.column('tahun_terbit', width="100")
        self.tree.heading('stok_buku', text='STOK_BUKU')
        self.tree.column('stok_buku', width="90")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtCode_buku.delete(0,END)
        self.txtCode_buku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun_terbit.delete(0,END)
        self.txtTahun_terbit.insert(END,"")
        self.txtStok_buku.delete(0,END)
        self.txtStok_buku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kode_buku"],d["code_buku"],d["judul"],d["penulis"],d["penerbit"],d["tahun_terbit"],d["stok_buku"]))
    def onCari(self, event=None):
        code_buku = self.txtCode_buku.get()
        obj = Buku()
        a = obj.get_by_code_buku(code_buku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        code_buku = self.txtCode_buku.get()
        obj = Buku()
        res = obj.get_by_code_buku(code_buku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.penulis)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahun_terbit.delete(0,END)
        self.txtTahun_terbit.insert(END,obj.tahun_terbit)
        self.txtStok_buku.delete(0,END)
        self.txtStok_buku.insert(END,obj.stok_buku)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        code_buku = self.txtCode_buku.get()
        judul = self.txtJudul.get()
        penulis = self.txtPenulis.get()
        penerbit = self.txtPenerbit.get()
        tahun_terbit = self.txtTahun_terbit.get()
        stok_buku = self.txtStok_buku.get()
        # create new Object
        obj = Buku()
        obj.code_buku = code_buku
        obj.judul = judul
        obj.penulis = penulis
        obj.penerbit = penerbit
        obj.tahun_terbit = tahun_terbit
        obj.stok_buku = stok_buku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_code_buku(code_buku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        code_buku = self.txtCode_buku.get()
        obj = Buku()
        obj.code_buku = code_buku
        if(self.ditemukan==True):
            res = obj.delete_by_code_buku(code_buku)
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
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()