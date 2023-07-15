import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Petugas import *
class FrmPetugas:
    
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
        Label(mainFrame, text='CODE_PETUGAS:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK_PETUGAS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JABATAN:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO_TELEPON:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtCode_petugas = Entry(mainFrame) 
        self.txtCode_petugas.grid(row=0, column=1, padx=5, pady=5)
        self.txtCode_petugas.bind("<Return>",self.onCari)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk_petugas = StringVar()
        Cbo_jk_petugas = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk_petugas) 
        Cbo_jk_petugas.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk_petugas combobox drop down list
        Cbo_jk_petugas['values'] = ('L','P')
        Cbo_jk_petugas.current()
        # Textbox
        self.txtJabatan = Entry(mainFrame) 
        self.txtJabatan.grid(row=3, column=1, padx=5, pady=5)
        self.txtNo_telpon = Entry(mainFrame) 
        self.txtNo_telpon.grid(row=4, column=1, padx=5, pady=5)
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
        columns = ('kode_petugas','code_petugas','nama','jk_petugas','jabatan','no_telepon','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('kode_petugas', text='KODE_PETUGAS')
        self.tree.column('kode_petugas', width="100")
        self.tree.heading('code_petugas', text='CODE_PETUGAS')
        self.tree.column('code_petugas', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('jk_petugas', text='JK_PETUGAS')
        self.tree.column('jk_petugas', width="100")
        self.tree.heading('jabatan', text='JABATAN')
        self.tree.column('jabatan', width="100")
        self.tree.heading('no_telepon', text='NO_TELEPON')
        self.tree.column('no_telepon', width="100")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="150")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtCode_petugas.delete(0,END)
        self.txtCode_petugas.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk_petugas.set("")
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,"")
        self.txtNo_telpon.delete(0,END)
        self.txtNo_telpon.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data petugas
        obj = Petugas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kode_petugas"],d["code_petugas"],d["nama"],d["jk_petugas"],d["jabatan"],d["no_telepon"],d["alamat"]))
    def onCari(self, event=None):
        code_petugas = self.txtCode_petugas.get()
        obj = Petugas()
        a = obj.get_by_code_petugas(code_petugas)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        code_petugas = self.txtCode_petugas.get()
        obj = Petugas()
        res = obj.get_by_code_petugas(code_petugas)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk_petugas.set(obj.jk_petugas)
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,obj.jabatan)
        self.txtNo_telpon.delete(0,END)
        self.txtNo_telpon.insert(END,obj.no_telepon)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        code_petugas = self.txtCode_petugas.get()
        nama = self.txtNama.get()
        jk_petugas = self.txtJk_petugas.get()
        jabatan = self.txtJabatan.get()
        no_telepon = self.txtNo_telpon.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Petugas()
        obj.code_petugas = code_petugas
        obj.nama = nama
        obj.jk_petugas = jk_petugas
        obj.jabatan = jabatan
        obj.no_telepon = no_telepon
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_code_petugas(code_petugas)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        code_petugas = self.txtCode_petugas.get()
        obj = Petugas()
        obj.code_petugas = code_petugas
        if(self.ditemukan==True):
            res = obj.delete_by_code_petugas(code_petugas)
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
    aplikasi = FrmPetugas(root2, "Aplikasi Data Petugas")
    root2.mainloop()
