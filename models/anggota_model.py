# Inayah Alghoni Wahyudin Abdeli (033)

from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table_name}")
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
            cursor.execute(query, (nama, alamat))
            self.conn.commit()
            cursor.close()
            return True

        except Exception as e:
            print("Gagal menambah anggota:", e)
            self.conn.rollback()
            return False

    def update_anggota(self, id_anggota, nama, alamat):
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()
            query = """
                UPDATE anggota
                SET nama = %s, alamat = %s
                WHERE id_anggota = %s
            """
            cursor.execute(query, (nama, alamat, id_anggota))
            self.conn.commit()
            cursor.close()
            return True

        except Exception as e:
            print("Gagal memperbarui anggota:", e)
            self.conn.rollback()
            return False

    def delete_anggota(self, id_anggota):
        if not self.conn:
            return False

        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM anggota WHERE id_anggota = %s"
            cursor.execute(query, (id_anggota,))
            self.conn.commit()
            cursor.close()
            return True

        except Exception as e:
            print("Gagal menghapus anggota:", e)
            self.conn.rollback()
            return False