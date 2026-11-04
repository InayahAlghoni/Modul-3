import hashlib
from mysql.connector import Error
from config.database import Database

class UserModel:
    ROLE_VALID = ("admin", "anggota")

    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Mengubah plain text password menjadi hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)

            # Parameterized Query untuk mencegah SQL Injection
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None

    def username_exists(self, username):
        # Cek apakah username sudah terdaftar
        if not self.conn:
            return False

        cursor = self.conn.cursor()
        cursor.execute(f"SELECT 1 FROM {self.table_name} WHERE username = %s", (username,))
        ada = cursor.fetchone() is not None
        cursor.close()
        return ada

    def register_user(self, username, password, role):
        # Password di-hash SHA-256 dulu, plain text tidak pernah disimpan ke database
        if not self.conn:
            return False

        # Role harus salah satu nilai yang dikenali sistem
        if role not in self.ROLE_VALID:
            return False

        try:
            cursor = self.conn.cursor()
            password_hash = self.hash_password(password)

            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password_hash, role))
            self.conn.commit()
            cursor.close()
            return True

        except Error as e:
            print("Gagal mendaftarkan user:", e)
            self.conn.rollback()
            return False
