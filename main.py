# ****************************************
# **           MENU PRINCIPAL          **
# ****************************************

def menu():
    opcion = 0
    intentos = 0
    while True:
        try:
            print("\n\t\t\t\t\t\t----------------------------")
            print("\t\t\t\t\t\t----- MENÚ DE OPCIONES -----")
            print("\t\t\t\t\t\t----------------------------")

            print("""\nSeleccione la opción de su preferencia:\n
            🔴 1.- Consultar usuario del directorio.\n
            🔴 2.- Consultar directorio.\n
            🔴 3.- Añadir contacto.\n
            🔴 4.- Cambiar teléfono.\n
            🔴 5.- Eliminar usuario.\n
            🔴 6.- Salir.\n""")

            opcion = int(input("--Dígite opción--> "))

            if 0 < opcion <= 6:
                return opcion
                break

            else:
                print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")
                intentos += 1
                if intentos <= 3:
                    if intentos == 1:
                        print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                    elif intentos == 2:
                        print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                    else:
                        print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                else:
                    print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                    print("\n********************* FIN DE MENU DE OPCIONES *********************")
                    return -1


        except ValueError:
            print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")


# ****************************************
# **        CONSULTA DE  USUARIOS       **
# ****************************************

def consultar_usuario(directorio):  # Funcion para consultar usuarios para la lista
    intentos = 0
    incremento = 1
    salir = False

    print("\n\t\t\t\t\t\t----------------------------")
    print("\t\t\t\t\t\t---- CONSULTAR CONTACTOS ---")
    print("\t\t\t\t\t\t----------------------------")
    for clave, valor in directorio.items():
        print(f"\n----------- CONTACTO NO. {incremento}  -----------")
        print(f"\t\t\t🔴 {incremento}.- {clave}")
        print("---------------------------------------")
        incremento += 1

    try:

        nombre = (input("\n--Dígite El nombre del contacto --> ").strip()).title()

        if nombre in directorio:
            print(f"\n--------------  CONTACTO {nombre.upper()}  -------------")
            print(f"🔴 Nombre: {nombre} --> Teléfono: {directorio[nombre]}")
            print("---------------------------------------------")

            while salir == False:
                print("""\n¿Desea volver a buscar algún usuario?\n
                🔴 1.- Si.\n
                🔴 2.- No.\n""")
                opcion = int(input("--Dígite opción--> "))

                if opcion == 1:
                    salir = True
                    consultar_usuario(directorio)

                elif opcion == 2:
                    salir = True

                else:
                    print(
                        "\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")
                    intentos += 1
                    if intentos <= 3:
                        if intentos == 1:
                            print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                            salir = False
                        elif intentos == 2:
                            print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                            salir = False
                        else:
                            print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                            salir = False
                    else:
                        print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                        print("\n********************* FIN DE CONSULTA DE USUARIO DE DIRECTORIO *********************")
                        salir = True


        else:
            print(
                f"\nERROR --> Oops!! \"{nombre.title()}\" no se encuentra dentro del directorio, vuelva a buscar el nombre del contacto.")
            consultar_usuario(directorio)

    except ValueError:
        print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")
        consultar_usuario(directorio)


# ****************************************
# **         CONSULTA DE DIRECTORIO     **
# ****************************************

def consultar(directorio):
    iterador = 1
    print("\n\t\t\t\t\t\t----------------------------")
    print("\t\t\t\t\t\t--- CONSULTAR DIRECTORIO ---")
    print("\t\t\t\t\t\t----------------------------")

    for clave, valor in directorio.items():
        print(f"\n* * * * *  CONTACTO NO. --> {iterador}   * * * * * * * * * *  ")
        print(f" Nombre: {clave} --> Teléfono: {valor} ")
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")
        iterador += 1


# ****************************************
# **          AGREGAR CONTACTOS         **
# ****************************************

def agregar_contacto(directorio):
	salir2 = False
	salir = False
	intentos = 0

	try:
		print("\n\t\t\t\t\t\t----------------------------")
		print("\t\t\t\t\t\t------ AÑADIR CONTACTO -----")
		print("\t\t\t\t\t\t----------------------------")

		nombre = (input("\n--Dígite su nombre --> ").strip()).title()
		telefono = input("\n--Dígite su número telefónico a 10 dígitos --> ").strip()
		if telefono.isdigit() and len(telefono) == 10:
			if nombre not in directorio:
				while salir == False:
					print(f"\nSe agregará a {nombre} con número teléfonico {telefono} ¿Esta de acuerdo?\n  "
						  f"\t\t🔴 1.- Si.\n"
						  
						  f"\t\t🔴 2.- No.\n")
					opcion = int(input("--Dígite opción--> "))
					if opcion == 1:
						directorio[nombre] = (telefono)
						print("\nUsuario agregado exitosamente!!")
						print("""¿Desea volver a agregar un nuevo contacto?\n
						🔴 1.- Si.\n
						🔴 2.- No.\n""")
						opcion = int(input("--Dígite opción--> "))
						if opcion==1:
							salir = True
							agregar_contacto(directorio)

						elif opcion==2:
							salir=True

						else:
							print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

							intentos += 1
							if intentos <= 3:
								if intentos == 1:
									print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
									salir = False
								elif intentos == 2:
									print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
									salir = False
								else:
									print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
									salir = False
							else:
								print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
								print("\n********************* FIN DE PROGRAMA *********************")
								salir = True
								return -1




					elif opcion == 2:
						salir = True
						agregar_contacto(directorio)

					else:
						print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

						intentos += 1
						if intentos <= 3:
							if intentos == 1:
								print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
								salir = False
							elif intentos == 2:
								print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
								salir = False
							else:
								print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
								salir = False
						else:
							print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
							print("\n********************* FIN DE PROGRAMA *********************")
							salir = True
							return -1



			else:
				while salir2 == False:
					print("""\nYa existe un contacto en la lista. ¿Desea reemplazarlo? \n
					🔴 1.- Si.
					🔴 2.- No.""")
					opcion = int(input("--Dígite opción--> "))

					if opcion == 1:
						directorio[nombre] = (telefono)
						print("\nContacto reemplazado exitosamente ")
						print("""¿Desea volver a agregar un nuevo contacto?\n
												🔴 1.- Si.\n						
												🔴 2.- No.\n""")
						opcion = int(input("--Dígite opción--> "))
						if opcion == 1:
							salir2 = True
							agregar_contacto(directorio)

						elif opcion == 2:
							salir2 = True

						else:
							print(
								"\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

							intentos += 1
							if intentos <= 3:
								if intentos == 1:
									print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
									salir2 = False
								elif intentos == 2:
									print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
									salir2 = False
								else:
									print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
									salir2 = False
							else:
								print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
								print("\n********************* FIN DE PROGRAMA *********************")
								salir2 = True
								return -1

					elif opcion == 2:
						salir2 = True
						agregar_contacto(directorio)

					else:
						print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

						intentos += 1
						if intentos <= 3:
							if intentos == 1:
								print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
								salir2 = False
							elif intentos == 2:
								print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
								salir2 = False
							else:
								print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
								salir2 = False
						else:
							print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
							print("\n********************* FIN DE PROGRAMA *********************")
							salir2 = True
							return -1

		else:
			print("\nLa cantidad de dígitos del número teléfonico no concuerda con el establecido a 10 dígitos. Verifique su respuesta. ")
			agregar_contacto(directorio)

	except ValueError:
			print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")
			agregar_contacto(directorio)


# ****************************************
# **          CAMBIAR TELEFONO          **
# ****************************************

def cambiar_telefono(directorio):  # Funcion para añadir usuarios a un diccionario llamado "directorio"
    salir, salir2 = False,False
    intentos = 0
    try:
        print("\n\t\t\t\t\t\t----------------------------")
        print("\t\t\t\t\t\t----- CAMBIAR TELÉFONO -----")
        print("\t\t\t\t\t\t----------------------------")
        nombre = (input("\n--Dígite su nombre --> ").strip()).title()
        telefono = input("\n--Dígite su número telefónico --> ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            if nombre in directorio:  # Si la variable "nombre" se encuentra en el diccionario  "directorio" entrará en esta condicional

                while salir == False:
                    print(f"""\nSe modifiicará el número del contacto: {nombre} por el nuevo número teléfonico: {telefono} ¿Esta de acuerdo?\n  
                    🔴 1.- Si.\n 
                    🔴 2.- No.\n""")
                    opcion = int(input("--Dígite opción--> "))
                    if opcion == 1:
                        directorio[nombre] = telefono #Se reemplaza el anterior numero por el nuevo
                        print("\nNúmero modificado exitosamente!!")
                        print("""¿Desea volver a modificar un nuevo teléfono?\n
                                    🔴 1.- Si.\n
                                    🔴 2.- No.\n""")
                        opcion = int(input("--Dígite opción--> "))
                        if opcion == 1:
                            salir = True
                            cambiar_telefono(directorio) #Vuelve a llamar a la funcion principal, recursividad

                        elif opcion == 2:
                            salir = True

                        else:
                            print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

                            intentos += 1
                            if intentos <= 3:
                                if intentos == 1:
                                    print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                                    salir = False
                                elif intentos == 2:
                                    print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                                    salir = False
                                else:
                                    print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                                    salir = False
                            else:
                                print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                                print("\n********************* FIN DE PROGRAMA *********************")
                                salir = True
                                return -1




                    elif opcion == 2:
                        salir = True
                        cambiar_telefono(directorio)

                    else:
                        print("\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

                        intentos += 1
                        if intentos <= 3:
                            if intentos == 1:
                                print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                                salir = False
                            elif intentos == 2:
                                print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                                salir = False
                            else:
                                print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                                salir = False
                        else:
                            print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                            print("\n********************* FIN DE PROGRAMA *********************")
                            salir = True
                            return -1



            else:
                while salir2 == False:
                    print("""\nNo existe un contacto con el nombre o telefono descrito. ¿Desea agregarlo? \n
                                🔴 1.- Si.
                                🔴 2.- No.""")
                    opcion = int(input("--Dígite opción--> "))

                    if opcion == 1:
                        salir2 = True
                        agregar_contacto(directorio)
                        '''directorio[nombre] = (telefono)
                        print("\nContacto reemplazado exitosamente ")
                        print("""¿Desea volver a agregar un nuevo contacto?\n
                                                            🔴 1.- Si.\n						
                                                            🔴 2.- No.\n""")
                        opcion = int(input("--Dígite opción--> "))'''
                        '''if opcion == 1:
                            salir2 = True
                            cambiar_telefono(directorio)

                        elif opcion == 2:
                            salir2 = True

                        else:
                            print(
                                "\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

                            intentos += 1
                            if intentos <= 3:
                                if intentos == 1:
                                    print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                                    salir2 = False
                                elif intentos == 2:
                                    print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                                    salir2 = False
                                else:
                                    print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                                    salir2 = False
                            else:
                                print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                                print("\n********************* FIN DE PROGRAMA *********************")
                                salir2 = True
                                return -1'''

                    elif opcion == 2:
                        salir2 = True
                        cambiar_telefono(directorio)

                    else:
                        print(
                            "\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")

                        intentos += 1
                        if intentos <= 3:
                            if intentos == 1:
                                print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                                salir2 = False
                            elif intentos == 2:
                                print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                                salir2 = False
                            else:
                                print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                                salir2 = False
                        else:
                            print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                            print("\n********************* FIN DE PROGRAMA *********************")
                            salir2 = True
                            return -1

        else:
            print("\nLa cantidad de dígitos del número teléfonico no concuerda con el establecido a 10 dígitos. Verifique su respuesta. ")
            cambiar_telefono(directorio)

    except ValueError:
        print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")
        cambiar_telefono(directorio)


# ****************************************
# **          ELIMINAR TELEFONO         **
# ****************************************

def eliminar(directorio):
    salir = False
    intentos = 0

    try:
        print("\n\t\t\t\t\t\t----------------------------")
        print("\t\t\t\t\t\t----- ELIMINAR TELÉFONO ----")
        print("\t\t\t\t\t\t----------------------------")
        nombre = (input("\n--Dígite su nombre --> ").strip()).title()
        if nombre in directorio:
            while salir == False:
                print(f"""{nombre} se eliminará ¿Está de acuerdo?\n
                🔴 1.- Si.\n 
                🔴 2.- No.\n""")
                opcion = int(input("--Dígite opción--> "))
                if opcion == 1:
                    print("Se ha eliminado el contacto exitosamente")
                    del directorio[nombre]
                    salir = True

                elif opcion == 2:
                    salir = True
                    eliminar(directorio)

                else:
                    print("ERROR --> Oops!! Se introdujo un valor fuera del rango del menú intente nuevamente. ")
                    intentos += 1
                    if intentos <= 3:
                        if intentos == 1:
                            print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                            salir = False
                        elif intentos == 2:
                            print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                            salir = False
                        else:
                            print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                            salir = False
                    else:
                        print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                        print("\n********************* FIN DE PROGRAMA *********************")
                        salir = True
                        return -1

        else:
            print("No se encuentra el contacto dentro del directorio.\n Intente nuevamente. ")
            eliminar(directorio)

    except ValueError:
        print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")


# ****************************************
# **     VOLVER AL MENU PRINCIPAL       **
# ****************************************

def menu_de_regreso():
    intentos = 0
    opcion = 0
    while True:
        try:
            print("\n************ RETORNO MENU PRINCIPAL ************ ")
            print("""\n¿Desea volver al menú principal?\n
			🔴 1.- Si.\n
			🔴 2.- No.\n""")
            opcion = int(input("--Dígite opción--> "))

            if 0 < opcion <= 2:
                return opcion
                break

            else:
                print(
                    "\nERROR --> Se ha introducido un valor diferente a los especificados dentro del menú de opciones. \n")
                intentos += 1
                if intentos <= 3:
                    if intentos == 1:
                        print(f"LLeva usted {intentos} intento, le quedán dos intentos más.")
                    elif intentos == 2:
                        print(f"LLeva usted {intentos} intentos, le quedá un intentos más.")
                    else:
                        print(f"LLeva usted {intentos} intentos, es su ultimo intento.")
                else:
                    print(f"El número de intentos permitidos han sido utilizados el programa se cerrará.")
                    print("\n********************* FIN DE PROGRAMA *********************")
                    return -1

        except ValueError:
            print("\nERROR --> Ha introducido una letra o espacio. Sólo se pueden agregar datos de tipo númerico.\nIntentelo nuevamente.\n ")


# ****************************************
# ****    PROGRAMA PRINCIPAL         *****
# ****************************************

directorio = {"Angel": "7788994455", "Angel2": "2238994455"}

while True:

    opcion = menu()

    if opcion == 1: # 🔴 1.- Consultar usuario del directorio.
        consultar_usuario(directorio)
        opcion = menu_de_regreso()
        if opcion == 1:
            continue
        elif opcion == -1:
            break
        else:
            break

    if opcion == 2: #🔴 2.- Consultar directorio.
        consultar(directorio)
        opcion = menu_de_regreso()
        if opcion == 1:
            continue
        elif opcion == -1:
            break
        else:
            break

    if opcion == 3: #🔴 3.- Añadir contacto.
        agregar_contacto(directorio)
        opcion = menu_de_regreso()
        if opcion == 1:
            continue
        elif opcion == -1:
            break
        else:
            break

    if opcion == 4: #🔴 4.- Cambiar teléfono.
        cambiar_telefono(directorio)
        opcion = menu_de_regreso()
        if opcion == 1:
            continue
        elif opcion == -1:
            break
        else:
            break

    if opcion == 5: #🔴 5.- Eliminar usuario.

        eliminar(directorio)

        opcion = menu_de_regreso()
        if opcion == 1:
            continue
        elif opcion == -1:
            break
        else:
            break


    if opcion == 6: #🔴 6.- Salir.
        break

    if opcion == -1: #Si menu retorna menos -1 se termina el programa
        break