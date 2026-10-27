# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Nombre y apellido:  .....................................
#  Comision:           .....................................
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CODIGO ACA
    # 1. Evitar comando vacio
    if len(comando) == 0:
        return False

    # 2. Verificacion de nombre valido
    nombre = comando[0]

    if nombre != "avanzar" and nombre != "girar" and nombre != "detenerse" and nombre != "saludar":
        return False

    # 3. Validacion sobre existencia de parametros V y T
    if nombre == "avanzar" or nombre == "girar":

        if len(comando) != 3:
            return False

        velocidad = comando[1]
        tiempo = comando[2]

        # 4. Verificacion tipo de caracter
        if type(velocidad) != int and type(velocidad) != float:
            return False

        if type(tiempo) != int and type(tiempo) != float:
            return False

        # 5. Verificar que el tiempo no sea negativo
        if tiempo < 0:
            return False

    # 6. Validar comandos sin parámetros
    else:
        if len(comando) != 1:
            return False

    return True
    pass


# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CODIGO ACA
    if not comando_es_valido(comando):
        return "Comando inválido"

    nombre = comando[0]

    try:
        if nombre == "avanzar":
            velocidad = comando[1]
            tiempo = comando[2]
            robot.avanzar(velocidad=velocidad, tiempo=tiempo)
            return "El robot avanzó correctamente"

        elif nombre == "girar":
            velocidad = comando[1]
            tiempo = comando[2]
            robot.girar(velocidad=velocidad, tiempo=tiempo)
            return "El robot giró correctamente"

        elif nombre == "detenerse":
            robot.detenerse()
            return "El robot se detuvo correctamente"

        elif nombre == "saludar":
            robot.saludar()
            return "El robot saludó correctamente"

    except ErrorDeSeguridad as error:
        return "Error de seguridad: " + str(error)

    pass


# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    # TU CODIGO ACA

    for comando in mision:

        if comando_es_valido(comando):
            resultado = ejecutar_comando(robot, comando)

        else:
            if len(comando) == 0:
                resultado = "Comando vacío"

            elif comando[0] != "avanzar" and comando[0] != "girar" and comando[0] != "detenerse" and comando[0] != "saludar":
                resultado = "Nombre de comando incorrecto"

            elif comando[0] == "avanzar" or comando[0] == "girar":

                if len(comando) != 3:
                    resultado = "Cantidad de parámetros incorrecta"

                elif type(comando[1]) != int and type(comando[1]) != float:
                    resultado = "La velocidad no es un número"

                elif type(comando[2]) != int and type(comando[2]) != float:
                    resultado = "El tiempo no es un número"

                elif comando[2] < 0:
                    resultado = "El tiempo no puede ser negativo"

            else:
                resultado = "Cantidad de parámetros incorrecta"

        historial.append(resultado)

    pass


# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    # TU CODIGO ACA
    correctos = 0
    rechazados = 0

    for resultado in historial:

        if resultado == "El robot avanzó correctamente" or resultado == "El robot giró correctamente" or resultado == "El robot se detuvo correctamente" or resultado == "El robot saludó correctamente":
            correctos += 1

        else:
            rechazados += 1
            print("Motivo del rechazo:", resultado)

    print("----- REPORTE FINAL -----")
    print("Comandos correctos:", correctos)
    print("Comandos rechazados:", rechazados)

    pass


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        # Empeza probando con MISION_BASICA.
        # Cuando funcione, proba con MISION_CON_ERRORES: esa tiene
        # comandos invalidos a proposito.
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
