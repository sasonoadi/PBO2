import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
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
        Label(mainFrame, text='CODE_ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK_ANGGOTA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JURUSAN:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO_TLP:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtCode_anggota = Entry(mainFrame) 
        self.txtCode_anggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtCode_anggota.bind("<Return>", self.onCari)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk_anggota = StringVar()
        Cbo_jk_anggota = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk_anggota) 
        Cbo_jk_anggota.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk_anggota combobox drop down list
        Cbo_jk_anggota['values'] = ('L','P')
        Cbo_jk_anggota.current()
        # Textbox
        self.txtJurusan = Entry(mainFrame) 
        self.txtJurusan.grid(row=3, column=1, padx=5, pady=5)
        self.txtNo_telepon = Entry(mainFrame) 
        self.txtNo_telepon.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('kode_anggota','code_anggota','nama','jk_anggota','jurusan','no_tlp','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('code_anggota', text='CODE_ANGGOTA')
        self.tree.column('code_anggota', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('jk_anggota', text='JK_ANGGOTA')
        self.tree.column('jk_anggota', width="80")
        self.tree.heading('jurusan', text='JURUSAN')
        self.tree.column('jurusan', width="70")
        self.tree.heading('no_tlp', text='NO_TLP')
        self.tree.column('no_tlp', width="100")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="150")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtCode_anggota.delete(0,END)
        self.txtCode_anggota.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk_anggota.set("")
        self.txtJurusan.delete(0,END)
        self.txtJurusan.insert(END,"")
        self.txtNo_telepon.delete(0,END)
        self.txtNo_telepon.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kode_anggota"],d["code_anggota"],d["nama"],d["jk_anggota"],d["jurusan"],d["no_tlp"],d["alamat"]))
    def onCari(self, event=None):
        code_anggota = self.txtCode_anggota.get()
        obj = Anggota()
        a = obj.get_by_code_anggota(code_anggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        code_anggota = self.txtCode_anggota.get()
        obj = Anggota()
        res = obj.get_by_code_anggota(code_anggota)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk_anggota.set(obj.jk_anggota)
        self.txtJurusan.delete(0,END)
        self.txtJurusan.insert(END,obj.jurusan)
        self.txtNo_telepon.delete(0,END)
        self.txtNo_telepon.insert(END,obj.no_tlp)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        code_anggota = self.txtCode_anggota.get()
        nama = self.txtNama.get()
        jk_anggota = self.txtJk_anggota.get()
        jurusan = self.txtJurusan.get()
        no_tlp = self.txtNo_telepon.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.code_anggota = code_anggota
        obj.nama = nama
        obj.jk_anggota = jk_anggota
        obj.jurusan = jurusan
        obj.no_tlp = no_tlp
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_code_anggota(code_anggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        code_anggota = self.txtCode_anggota.get()
        obj = Anggota()
        obj.code_anggota = code_anggota
        if(self.ditemukan==True):
            res = obj.delete_by_code_anggota(code_anggota)
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()
