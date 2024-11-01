import tkinter as tk
from tkinter import messagebox, simpledialog
from user_management import UserManagement
from invoice_management import InvoiceManagement
from reporting import Reporting
from datetime import datetime

class ClubDeportivoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema Administrativo - Club Deportivo")
        
        # Inicialización de la base de datos
        self.db_name = "club_deportivo.db"
        self.user_management = UserManagement(self.db_name)
        self.invoice_management = InvoiceManagement(self.db_name)
        self.reporting = Reporting(self.db_name)

        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Botones de gestión de usuarios
        self.btn_add_user = tk.Button(self.master, text="Agregar Usuario", command=self.add_user)
        self.btn_add_user.pack(pady=10)

        self.btn_view_users = tk.Button(self.master, text="Ver Usuarios", command=self.view_users)
        self.btn_view_users.pack(pady=10)

        # Botones de gestión de facturas
        self.btn_generate_invoice = tk.Button(self.master, text="Generar Factura", command=self.generate_invoice)
        self.btn_generate_invoice.pack(pady=10)

        self.btn_view_invoices = tk.Button(self.master, text="Ver Facturas", command=self.view_invoices)
        self.btn_view_invoices.pack(pady=10)

        # Botones de reportes
        self.btn_monthly_report = tk.Button(self.master, text="Generar Reporte Mensual", command=self.generate_monthly_report)
        self.btn_monthly_report.pack(pady=10)

        self.btn_exit = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.btn_exit.pack(pady=10)

    def add_user(self):
        # Solicitar información del usuario
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre:")
        apellido = simpledialog.askstring("Apellido", "Ingrese el apellido:")
        fecha_de_nacimiento = simpledialog.askstring("Fecha de Nacimiento", "Ingrese la fecha de nacimiento (YYYY-MM-DD):")
        direccion = simpledialog.askstring("Dirección", "Ingrese la dirección:")
        telefono = simpledialog.askstring("Teléfono", "Ingrese el teléfono:")
        correo = simpledialog.askstring("Correo", "Ingrese el correo electrónico:")
        rol = simpledialog.askstring("Rol", "Ingrese el rol (socio, no socio, invitado):")
        fecha_de_inscripcion = datetime.now().strftime('%Y-%m-%d')

        # Agregar usuario
        if self.user_management.add_user(nombre, apellido, fecha_de_nacimiento, direccion, telefono, correo, rol, fecha_de_inscripcion):
            messagebox.showinfo("Éxito", "Usuario agregado exitosamente.")
        else:
            messagebox.showerror("Error", "El correo ya está en uso.")

    def view_users(self):
        users = self.user_management.get_users()
        user_list = "\n".join([f"{u[0]}: {u[1]} {u[2]} - {u[6]}" for u in users])
        messagebox.showinfo("Usuarios", user_list if user_list else "No hay usuarios registrados.")

    def generate_invoice(self):
        user_id = simpledialog.askinteger("ID de Usuario", "Ingrese el ID del usuario:")
        monto = simpledialog.askfloat("Monto", "Ingrese el monto de la factura:")
        mes_facturacion = datetime.now().strftime('%Y-%m')

        # Generar factura
        self.invoice_management.generate_invoice(user_id, monto, mes_facturacion)
        messagebox.showinfo("Éxito", "Factura generada exitosamente.")

    def view_invoices(self):
        user_id = simpledialog.askinteger("ID de Usuario", "Ingrese el ID del usuario:")
        invoices = self.invoice_management.get_invoices_by_user(user_id)
        invoice_list = "\n".join([f"Factura ID {i[0]}: Monto {i[1]}, Fecha {i[3]}, Mes {i[4]}" for i in invoices])
        messagebox.showinfo("Facturas", invoice_list if invoice_list else "No hay facturas registradas para este usuario.")

    def generate_monthly_report(self):
        report_data = self.reporting.get_monthly_report()
        self.reporting.save_report_to_txt(report_data, "reporte_mensual.txt")
        messagebox.showinfo("Reporte Mensual", "Reporte mensual generado y guardado en 'reporte_mensual.txt'.")

    def on_closing(self):
        self.user_management.close()
        self.invoice_management.close()
        self.reporting.close()
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClubDeportivoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
