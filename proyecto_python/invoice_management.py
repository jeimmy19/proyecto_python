import sqlite3
from datetime import datetime

class InvoiceManagement:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Crear tabla de facturas si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                monto REAL NOT NULL,
                fecha DATE NOT NULL,
                mes_facturacion TEXT NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
            )
        ''')
        self.connection.commit()

    def generate_invoice(self, user_id, monto, mes_facturacion):
        fecha = datetime.now().date()
        self.cursor.execute('''
            INSERT INTO facturas (id_usuario, monto, fecha, mes_facturacion)
            VALUES (?, ?, ?, ?)
        ''', (user_id, monto, fecha, mes_facturacion))
        self.connection.commit()

    def get_invoices_by_user(self, user_id):
        self.cursor.execute('SELECT * FROM facturas WHERE id_usuario = ?', (user_id,))
        return self.cursor.fetchall()

    def get_all_invoices(self):
        self.cursor.execute('SELECT * FROM facturas')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
