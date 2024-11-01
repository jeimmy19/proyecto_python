import sqlite3

class UserManagement:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        # Crear tabla de usuarios si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                fecha_de_nacimiento TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                rol TEXT NOT NULL,
                fecha_de_inscripcion TEXT NOT NULL,
                id_socio_invitador INTEGER,
                FOREIGN KEY (id_socio_invitador) REFERENCES usuarios (id)
            )
        ''')
        self.connection.commit()

    def add_user(self, nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion, id_socio_invitador=None):
        try:
            self.cursor.execute('''
                INSERT INTO usuarios (nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion, id_socio_invitador)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion, id_socio_invitador))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Correo duplicado

    def edit_user(self, user_id, nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion, id_socio_invitador=None):
        self.cursor.execute('''
            UPDATE usuarios
            SET nombre = ?, apellido = ?, fecha_de_nacimiento = ?, direccion = ?, telefono = ?, correo = ?, rol = ?, fecha_de_inscripcion = ?, id_socio_invitador = ?
            WHERE id = ?
        ''', (nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion, id_socio_invitador, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
        self.connection.commit()

    def get_users(self):
        self.cursor.execute('SELECT * FROM usuarios')
        return self.cursor.fetchall()

    def get_user_by_id(self, user_id):
        self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()
