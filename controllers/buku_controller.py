# Inayah Alghoni Wahyudin Abdeli_033
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding tombol & event tabel
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_perbarui.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input, tombol simpan, perbarui, dan hapus
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_perbarui.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def pilih_data(self, event=None):
        selected_item = self.view.tabel.selection()

        if not selected_item:
            return

        values = self.view.tabel.item(selected_item[0], "values")

        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, values[1])

        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, values[2])

        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, values[3])

    def perbarui_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        # Mengambil baris yang dipilih
        selected_item = self.view.tabel.selection()

        if not selected_item:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui dari tabel!"
            )
            return

        # Mengambil ID dari kolom pertama
        values = self.view.tabel.item(selected_item[0], "values")
        id_buku = values[0]

        # Mengambil data terbaru dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi form
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Meminta Model memperbarui data berdasarkan ID
        berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil diperbarui!"
            )
            self.muat_data_tabel()

            # Membersihkan form setelah berhasil
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")
        else:
            messagebox.showerror(
                "Error", "Data buku gagal diperbarui."
            )

        
    def hapus_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        # Mengambil baris yang dipilih
        selected_item = self.view.tabel.selection()

        if not selected_item:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus dari tabel!"
            )
            return

        # Mengambil ID buku dari kolom pertama
        values = self.view.tabel.item(selected_item[0], "values")
        id_buku = values[0]

        # Meminta konfirmasi sebelum menghapus
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Apakah kamu yakin ingin menghapus buku ID {id_buku}?"
        )

        if not konfirmasi:
            return

        # Meminta Model menghapus buku berdasarkan ID
        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses", "Data buku berhasil dihapus!"
            )
            self.muat_data_tabel()

            # Membersihkan form
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")
        else:
            messagebox.showerror(
                "Error", "Data buku gagal dihapus."
            )



    def logout(self):
        # Tutup jendela perpustakaan, lalu kembali ke jendela Login
        self.view.destroy()
        # Import di dalam fungsi untuk menghindari circular import
        # (auth_controller sudah meng-import buku_controller di level modul)
        from controllers.auth_controller import AuthController
        AuthController().run()

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()

