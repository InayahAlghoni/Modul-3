import customtkinter as ctk

class RegisterView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Daftar Akun - Sistem Perpustakaan")
        self.geometry("360x420")
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.frame, text="DAFTAR AKUN", font=("Arial", 18, "bold")).pack(pady=(20, 15))

        self.entry_username = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.entry_username.pack(pady=10, padx=20, fill="x")

        self.entry_password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.entry_password.pack(pady=10, padx=20, fill="x")

        self.entry_konfirmasi = ctk.CTkEntry(self.frame, placeholder_text="Konfirmasi Password", show="*")
        self.entry_konfirmasi.pack(pady=10, padx=20, fill="x")

        self.btn_daftar = ctk.CTkButton(self.frame, text="Daftar", fg_color="green")
        self.btn_daftar.pack(pady=(20, 10), padx=20, fill="x")

        self.btn_kembali = ctk.CTkButton(self.frame, text="Kembali ke Login", fg_color="gray")
        self.btn_kembali.pack(pady=(0, 20), padx=20, fill="x")
