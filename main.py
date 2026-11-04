# Inayah Alghoni Wahyudin Abdeli_033
import customtkinter as ctk

class MenuUtama(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("350x250")
        self.pilihan = None

        ctk.CTkLabel(
            self, text="Pilih Data yang Dikelola", font=("Arial", 16, "bold")
        ).pack(pady=25)

        ctk.CTkButton(
            self, text="Data Buku", command=lambda: self.pilih("buku")
        ).pack(pady=10, padx=40, fill="x")

        ctk.CTkButton(
            self, text="Data Anggota", command=lambda: self.pilih("anggota")
        ).pack(pady=10, padx=40, fill="x")

    def pilih(self, nama):
        self.pilihan = nama
        self.destroy()  # tutup menu agar mainloop berhenti

from controllers.auth_controller import AuthController

if __name__ == "__main__":
    app = AuthController()
    app.run()