import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.register_view import RegisterView

class RegisterController:
    MIN_USERNAME = 3
    MIN_PASSWORD = 6
    # Pendaftaran mandiri selalu menghasilkan akun anggota (admin tidak bisa dipilih sendiri)
    ROLE_DEFAULT = "anggota"

    def __init__(self):
        self.model = UserModel()
        self.view = RegisterView()
        self.view.btn_daftar.configure(command=self.proses_daftar)
        self.view.btn_kembali.configure(command=self.kembali_ke_login)

    def proses_daftar(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()
        konfirmasi = self.view.entry_konfirmasi.get()

        if not username or not password or not konfirmasi:
            messagebox.showwarning("Peringatan", "Semua kolom wajib diisi!")
            return

        if len(username) < self.MIN_USERNAME:
            messagebox.showwarning("Peringatan", f"Username minimal {self.MIN_USERNAME} karakter!")
            return

        if len(password) < self.MIN_PASSWORD:
            messagebox.showwarning("Peringatan", f"Password minimal {self.MIN_PASSWORD} karakter!")
            return

        if password != konfirmasi:
            messagebox.showwarning("Peringatan", "Konfirmasi password tidak sama!")
            return

        if self.model.username_exists(username):
            messagebox.showerror("Gagal", "Username sudah digunakan, pilih username lain!")
            return

        if self.model.register_user(username, password, self.ROLE_DEFAULT):
            messagebox.showinfo("Sukses", "Akun berhasil dibuat! Silakan login.")
            self.kembali_ke_login()
        else:
            messagebox.showerror("Error", "Pendaftaran gagal. Coba lagi.")

    def kembali_ke_login(self):
        self.view.destroy()
        # Import di dalam fungsi untuk menghindari circular import
        from controllers.auth_controller import AuthController
        AuthController().run()

    def run(self):
        self.view.mainloop()
