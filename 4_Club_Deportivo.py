class ClubDeportivo:
    def __init__(self):
        self.socios = []
        self.profesores = []
        self.deportes = {"Futbol": [], "Tenis": [], "Natacion": []}
        self.invitados = []
        self.rendicion_cuentas = []

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

    def menu_principal(self, rol):
        while True:
            print("\n== Menú Principal ==")
            print("1. Gestion de Socios")
            print("2. Gestion de Profesores")
            print("3. Gestionar Deportes")
            print("4. Gestionar Entradas a Torneos")
            if rol == "admin" or rol == "contador":
                print("5. Rendición de Cuentas")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestion_socios()
            elif opcion == "2" and rol != "contador":
                self.gestion_profesores()
            elif opcion == "3" and rol != "contador":
                self.gestion_deportes()
            elif opcion == "4" and rol != "contador":
                self.gestion_entradas_torneos()
            elif opcion == "5" and rol == "contador":
                self.ver_rendicion_cuentas()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida o sin permisos.")

    def gestion_socios(self):
        while True:
            print("\n== Gestión de Socios ==")
            print("a) Registrar Socio")
            print("b) Pagar Cuota de Socio")
            print("c) Dar de Baja Socio")
            print("d) Pagar Cuota Deportiva")
            print("e) Lista de Socios")
            print("g) Registrar Invitado")
            print("h) Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "a":
                self.registrar_socio()
            elif opcion == "b":
                self.pagar_cuota_socio()
            elif opcion == "c":
                self.dar_baja_socio()
            elif opcion == "d":
                self.pagar_cuota_deportiva()
            elif opcion == "e":
                self.lista_socios()
            elif opcion == "g":
                self.registrar_invitado()
            elif opcion == "h":
                break
            else:
                print("Opción no válida.")

    def gestion_profesores(self):
        while True:
            print("\n== Gestión de Profesores ==")
            print("a) Agregar Profesor")
            print("b) Eliminar Profesor")
            print("c) Listar Profesores")
            print("d) Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "a":
                self.agregar_profesor()
            elif opcion == "b":
                self.eliminar_profesor()
            elif opcion == "c":
                self.listar_profesores()
            elif opcion == "d":
                break
            else:
                print("Opción no válida.")

    def gestion_deportes(self):
        while True:
            print("\n== Gestión de Deportes ==")
            print("a) Lista Futbol")
            print("b) Lista Tenis")
            print("c) Lista Natacion")
            print("d) No Socio")
            print("e) Pagar Cuota Deportiva No Socio")
            print("f) Dar de Baja No Socio")
            print("g) Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "a":
                self.lista_deporte("Futbol")
            elif opcion == "b":
                self.lista_deporte("Tenis")
            elif opcion == "c":
                self.lista_deporte("Natacion")
            elif opcion == "d":
                self.registrar_no_socio()
            elif opcion == "e":
                self.pagar_cuota_deportiva_no_socio()
            elif opcion == "f":
                self.dar_baja_no_socio()
            elif opcion == "g":
                break
            else:
                print("Opción no válida.")

    def gestion_entradas_torneos(self):
        while True:
            print("\n== Gestión de Entradas a Torneos ==")
            print("1) Entrada Futbol Socio")
            print("2) Entrada Futbol No Socio")
            print("3) Entrada Tenis Socio")
            print("4) Entrada Tenis No Socio")
            print("5) Entrada Natacion Socio")
            print("6) Entrada Natacion No Socio")
            print("7) Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.entrada_estadio("Futbol", "socio")
            elif opcion == "2":
                self.entrada_estadio("Futbol", "no_socio")
            elif opcion == "3":
                self.entrada_estadio("Tenis", "socio")
            elif opcion == "4":
                self.entrada_estadio("Tenis", "no_socio")
            elif opcion == "5":
                self.entrada_estadio("Natacion", "socio")
            elif opcion == "6":
                self.entrada_estadio("Natacion", "no_socio")
            elif opcion == "7":
                break
            else:
                print("Opción no válida.")

    def ver_rendicion_cuentas(self):
        print("\n== Rendición de Cuentas ==")
        for item in self.rendicion_cuentas:
            print(item)

    # Métodos específicos para cada acción

    def registrar_socio(self):
        nombre = input("Nombre del socio: ")
        cuota = float(input("Cuota inicial: "))
        self.socios.append({"nombre": nombre, "cuota": cuota})
        self.rendicion_cuentas.append(
            f"Cuota de socio pagada por {nombre}: ${cuota}")
        print(f"Socio {nombre} registrado con éxito.")

    def pagar_cuota_socio(self):
        nombre = input("Nombre del socio: ")
        for socio in self.socios:
            if socio["nombre"] == nombre:
                monto = float(input("Monto de la cuota: "))
                socio["cuota"] += monto
                self.rendicion_cuentas.append(
                    f"Cuota de socio pagada por {nombre}: ${monto}")
                print(f"Cuota de socio actualizada para {nombre}.")
                return
        print("Socio no encontrado.")

    def dar_baja_socio(self):
        nombre = input("Nombre del socio a dar de baja: ")
        self.socios = [
            socio for socio in self.socios if socio["nombre"] != nombre]
        print(f"Socio {nombre} dado de baja.")

    def pagar_cuota_deportiva(self):
        nombre = input("Nombre del socio: ")
        monto = float(input("Monto de la cuota deportiva: "))
        self.rendicion_cuentas.append(
            f"Cuota deportiva pagada por {nombre}: ${monto}")
        print(f"Cuota deportiva registrada para {nombre}.")

    def lista_socios(self):
        print("Lista de socios:")
        for socio in self.socios:
            print(socio["nombre"], "- Cuota total:", socio["cuota"])

    def registrar_invitado(self):
        nombre = input("Nombre del invitado: ")
        self.invitados.append(nombre)
        print(f"Invitado {nombre} registrado.")

    def agregar_profesor(self):
        nombre = input("Nombre del profesor: ")
        self.profesores.append(nombre)
        print(f"Profesor {nombre} agregado.")

    def eliminar_profesor(self):
        nombre = input("Nombre del profesor a eliminar: ")
        self.profesores = [prof for prof in self.profesores if prof != nombre]
        print(f"Profesor {nombre} eliminado.")

    def listar_profesores(self):
        print("Lista de profesores:")
        for profesor in self.profesores:
            print(profesor)

    def lista_deporte(self, deporte):
        print(f"Lista de inscritos en {deporte}:")
        for socio in self.deportes[deporte]:
            print(socio)

    def registrar_no_socio(self):
        nombre = input("Nombre del no socio: ")
        deporte = input("Deporte (Futbol, Tenis, Natacion): ")
        self.deportes[deporte].append(nombre)
        print(f"No socio {nombre} registrado en {deporte}.")

    def pagar_cuota_deportiva_no_socio(self):
        nombre = input("Nombre del no socio: ")
        monto = float(input("Monto de la cuota deportiva: "))
        self.rendicion_cuentas.append(
            f"Cuota deportiva no socio por {nombre}: ${monto}")
        print(f"Cuota deportiva registrada para no socio {nombre}.")

    def dar_baja_no_socio(self):
        nombre = input("Nombre del no socio a dar de baja: ")
        for deporte in self.deportes:
            self.deportes[deporte] = [
                ns for ns in self.deportes[deporte] if ns != nombre]
        print(f"No socio {nombre} dado de baja.")

    def entrada_estadio(self, deporte, tipo_socio):
        print(f"Entrada a {deporte} para {tipo_socio} registrada.")


# Ejecución del sistema
club = ClubDeportivo()
club.menu_ingreso()
