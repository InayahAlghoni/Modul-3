# Inayah Alghoni Wahyudin Abdeli_033
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data)

        self.muat_data_tabel()

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for a in self.model.get_all_anggota():
            self.view.tabel.insert(
                "", "end",
                values=(a['id_anggota'], a['nama'], a['alamat'])
            )

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def pilih_data(self, event=None):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            return

        values = self.view.tabel.item(selected_item[0], "values")

        self.bersihkan_form()
        self.view.entry_nama.insert(0, values[1])
        self.view.entry_alamat.insert(0, values[2])

    def perbarui_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih anggota yang ingin diperbarui dari tabel!")
            return

        id_anggota = self.view.tabel.item(selected_item[0], "values")[0]
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.muat_data_tabel()
            self.bersihkan_form()
        else:
            messagebox.showerror("Error", "Data anggota gagal diperbarui.")

    def hapus_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih anggota yang ingin dihapus dari tabel!")
            return

        id_anggota = self.view.tabel.item(selected_item[0], "values")[0]

        if not messagebox.askyesno(
            "Konfirmasi",
            f"Apakah kamu yakin ingin menghapus anggota ID {id_anggota}?"
        ):
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.muat_data_tabel()
            self.bersihkan_form()
        else:
            messagebox.showerror("Error", "Data anggota gagal dihapus.")

    def run(self):
        self.view.mainloop()