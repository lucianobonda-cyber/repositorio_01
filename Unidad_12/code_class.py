try:
    n = ["e", "4"]
    print(int(n[0]))
except IndexError:
    print("Indice fuera de rango")
except ValueError:
    print("algun digito es invalido")
except Exception as error:
    print(error)