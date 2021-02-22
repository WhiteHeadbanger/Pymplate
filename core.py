class ClassTemplate:
    def __init__(self, name: str, params: list):
        classargs = ', '.join(params)
        self._class = "class {}:\n\tdef __init__(self, {}):\n\t\tpass".format(name, classargs)

    def __str__(self):
        return self._class
        
class FunctionTemplate:
    def __init__(self, name: str, params: list):
        funcargs = ', '.join(params)
        self._func = "def {}({}):\n\tpass".format(name, funcargs)

    def __str__(self):
        return self._func


def write_to_func(instance):
    with open("p.py", "a+") as f:
        f.write("{}\n\n".format(str(instance)))


def main():
    while True:
        print(
            """
            1. Class
            2. Function
            3. Salir
            """
        )
        opc = int(input(">: "))
        if opc == 1:
            name = str(input("Nombre: "))
            args = []
            argcount = int(input("Numero de argumentos: "))
            for i in range(argcount):
                arg = str(input("Arg: "))
                args.append(arg)
            
            __class = ClassTemplate(name, args)
            write_to_func(__class)
        elif opc == 2:
            name = str(input("Nombre: "))
            args = []
            argcount = int(input("Numero de argumentos: "))
            for i in range(argcount):
                arg = str(input("Arg: "))
                args.append(arg)
            
            __func = FunctionTemplate(name, args)
            write_to_func(__func)
        elif opc == 3:
            return False
        else:
            print("No existe esa opcion")

main()



