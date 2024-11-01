import sqlite3

class Reporting:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_monthly_report(self):
        self.cursor.execute('''
            SELECT
                (SELECT COUNT(*) FROM usuarios WHERE rol = 'socio') AS total_socios,
                (SELECT COUNT(*) FROM usuarios WHERE rol = 'no socio') AS total_no_socios,
                (SELECT COUNT(*) FROM usuarios WHERE rol = 'invitado') AS total_invitados,
                (SELECT SUM(monto) FROM facturas) AS total_ingresos
        ''')
        return self.cursor.fetchone()

    def get_invoices_by_sport(self, sport):
        # Asumiendo que el deporte está relacionado a los usuarios por su rol
        self.cursor.execute('''
            SELECT COUNT(*) AS cantidad_facturas, SUM(monto) AS total_ingresos
            FROM facturas
            JOIN usuarios ON facturas.id_usuario = usuarios.id
            WHERE usuarios.rol IN ('socio', 'no socio') -- Suponiendo que los deportes son para estos roles
        ''')
        return self.cursor.fetchall()

    def save_report_to_txt(self, report_data, filename):
        with open(filename, 'w') as file:
            file.write("Reporte Mensual\n")
            file.write("===================\n")
            file.write(f"Total Socios: {report_data[0]}\n")
            file.write(f"Total No Socios: {report_data[1]}\n")
            file.write(f"Total Invitados: {report_data[2]}\n")
            file.write(f"Total Ingresos: {report_data[3]}\n")

    def close(self):
        self.connection.close()
