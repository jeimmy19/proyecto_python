import sqlite3

class Database:
    def __init__(self, db_name='club_deportivo.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Crear tabla de usuarios
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                fecha_de_nacimiento TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                rol TEXT NOT NULL CHECK (rol IN ('socio', 'no socio', 'invitado')),
                fecha_de_inscripcion TEXT NOT NULL,
                id_socio_invitador INTEGER,
                FOREIGN KEY (id_socio_invitador) REFERENCES usuarios (id)
            )
        ''')

        # Crear tabla de pagos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pagos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                fecha_pago TEXT NOT NULL,
                monto REAL NOT NULL,
                metodo_pago TEXT NOT NULL CHECK (metodo_pago IN ('efectivo', 'tarjeta', 'transferencia')),
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
            )
        ''')

        # Crear tabla de facturas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                mes INTEGER NOT NULL,
                año INTEGER NOT NULL,
                monto REAL NOT NULL,
                estado TEXT NOT NULL CHECK (estado IN ('pagada', 'no pagada')),
                FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
            )
        ''')

        self.connection.commit()

    def close(self):
        self.connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    db = Database()
    print("Base de datos y tablas creadas.")
    db.close()
