import pyodbc

class ClubDeportivo:
    def __init__(self):
        self.socios = []
        self.profesores = []
        self.deportes = {"Futbol": [], "Tenis": [], "Natacion": []}
        self.invitados = []
        self.rendicion_cuentas = []

    def conectar_sql_server(self):
        try:
            # Conexión a la base de datos SQL Server
            conexion = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=SQLEXPRESS;'  # nombre del servidor en la PC
                'DATABASE=Club Deportivo sql server;'
                'UID=Luis;'       # usuario de SQL Server en la PC tambien tienen que tener el usuario de su PC o crear uno para usar lo mismo
                'PWD= '      # contraseña de SQL Server en la PC
            )
            print("Conexión exitosa a la base de datos ClubDeportivo.")
            
            # Crea un cursor para ejecutar comandos SQL
            cursor = conexion.cursor()
            
            # Consulta para obtener las tablas
            cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
            
            # Mostrar el listado de tablas
            print("Tablas en la base de datos ClubDeportivo:")
            for row in cursor.fetchall():
                print(row[0])
            
            # Cerrar la conexión
            cursor.close()
            conexion.close()
        
        except Exception as e:
            print("Error al conectarse a SQL Server:", e)

    def menu_ingreso(self):
        print("== Sistema Administrativo del Club Deportivo ==")
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        if usuario == "admin" and contrasena == "1234":
            self.menu_principal("admin")
        elif usuario == "contador" and contrasena == "1234":
            self.menu_principal("contador")
        elif usuario == "recep" and contrasena == "1234":
            self.menu_principal("recepcionista")
        else:
            print("Usuario o contraseña incorrectos.")
            self.menu_ingreso()

    # aqui se tiene que agregar las funciones o los def del programa principal

# Ejecución del sistema y conexión a la base de datos
club = ClubDeportivo()
club.conectar_sql_server()  # Llamada al método para conectar y mostrar tablas
club.menu_ingreso()
