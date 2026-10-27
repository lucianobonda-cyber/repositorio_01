from src.datos import usuarios
import src.services as services
import src.interface as interface

def main():
    try:
        while True:
            print("\n  --- Gestión de Usuarios ---")
            print("  1. Crear usuario")
            print("  2. Ver usuarios")
            print("  3. Ver usuario por ID")
            print("  0. Volver")

            opcion = input("\n  Opción: ").strip()
            if opcion == "1":
                resultado = services.crear_usuario(usuarios)
                print(resultado)
            elif opcion == "2":
                interface.mostrar_usuarios(usuarios)
            elif opcion == "3":
                usuario = services.buscar_usuario_por_id(usuarios)
                print(usuario) if usuario else print("ID no encontrado")
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
    except Exception as e:
        print(e)


# ============================================================
if __name__ == "__main__":
    main()
