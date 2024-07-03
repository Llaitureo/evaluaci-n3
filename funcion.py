import os, time, csv

registros = []


def menu():
    while True:
        os.system('cls')
        print('\tMENÚ GAXPLOSIVE')
        print('opc.1 = Registrar pedido.')
        print('opc.2 = Mostrar todos los pedidos.')
        print('opc.3 = Buscar pedido por rut.')
        print('opc.4 = Imprimir hoja ruta.')
        print('opc.5 = Salir.')

        opc = int(input('ingrese opción:'))

        if opc in (1,2,3,4,5):
            os.system('cls')
            if opc == 1:
                opc_1()
            elif opc == 2:
                opc_2()
            elif opc == 3:
                opc_3()
            elif opc == 4:
                opc_4()
            else:
                print('adios..')
                return
            time.sleep(4)
        else:
            print('opción incorrecta..')
            time.sleep(2)

def opc_1():
    cil5=12500
    cil15=25500
    total2=0
    cant5=0
    cant15=0
    registro = {}
    print('\tREGISTRO PEDIDO')
    
    while True:
        try:
            rut = int(input('ingrese Rut, sin puntos ni guion: '))
            if len(str(rut))>3:
                break
            else:
                print('error, dígitos, no carácteres.')
        except:
            print('error.')

    while True:
        nombre = input('ingrese nombre: ')
        if len(nombre)>=3 and nombre.split():
                break
        else:
            print('el nombre debe tener 3 carácteres minimo.')
    
    while True:
        direccion = input('ingrese dirección: ')
        if len(direccion)>3 and direccion.split():
                break
        else:
            print('la dirección debe tener 3 carácteres minimo.')

    while True:
        comuna = input('ingrese comuna: ')
        if len(comuna)>=3 and comuna.split():
                break
        else:
            print('la comuna debe tener 3 carácteres minimo.')


    print('listo!')
    time.sleep(3)
    os.system('cls')

    print('\tTIPO PEDIDO')
    print('galones de 5kg(opc 1) y 15kg(opc 2) solamente.')
    while True:
        while True:
            try:
                pedido = int(input('ingrese el tipo del galon de gas a comprar: '))
                if pedido in (1,2):
                    break
            except:
                print('incorreto.')
            
        while True:
            try:
                cantidad = int(input('ingrese la cantidad de los cilindros a comprar: '))
                if pedido>0:
                    break
            except:
                print('incorreto.')

        if pedido ==1:
            total= cantidad * cil5
            cant5=+ 1
        else:
            total= cantidad * cil15
            cant15=+ 1
        
        total2=+ total

        while True:
            try:
                termino= int(input('desea dejar de añadir? SI=1, NO=2 :'))
                if termino in (1,2):
                    break
                else:
                    print('error..')
            except:
                print('error..')

        if termino in (1,2):
            if termino ==1:
                break
            else:
                pass
        else:
            print('opción incorrecta..')
        
        
    registro = {'rut':rut,
            'nombre':nombre,
            'direccion':direccion,
            'comuna':comuna,
            'pedido':pedido,
            'cantidad':cantidad,
            'total':total2,
            'cant5':cant5,
            'cant15':cant15}
    
    registros.append(registro)
    
    print('listo!')
    time.sleep(2)

def opc_2():
    if len(registros)==0:
        print('añade antes un registro.')
    else:
        print('\tMOSTRAR PEDIDOS')
        for x in registros:
            print(f'\n/RUT/{x['rut']}     /NOMBRE/{x['nombre']}        /DIRECCIÓN/{x['direccion']}       /COMUNA/{x['comuna']}      /CANT. CIL5/{x['cant5']}        /CANT. CIL15/{x['cant15']}          /TOTAL/{x['total']}')

def opc_3():
    if len(registros)==0:
        print('añade antes un registro.')
    else:
        print('\tBUSQUEDA POR RUT')
        while True:
            busquedar = int(input('ingrese el rut a buscar, sin puntos ni guión: '))
            if len(str(busquedar))==9:
                break
            else:
                print('no es un rut. el rut tiene 9 dígitos sin puntos ni guion')

        for elemento in registros:
            if elemento["rut"]==busquedar:
                print(f'\n/RUT/{elemento['rut']}     /NOMBRE/{elemento['nombre']}        /DIRECCIÓN/{elemento['direccion']}       /COMUNA/{elemento['comuna']}      /CANT. CIL5/{elemento['cant5']}        /CANT. CIL15/{elemento['cant15']}          /TOTAL/{elemento['total']}')
            
def opc_4():
    if len(registros)==0:
        print('añade antes un registro.')
    else:
        print('\tIMPRESORA DE RUTA')
        while True:
            busqueda = (input('ingrese el nombre de la comuna a buscar e imprimir: '))
            if len(busqueda)>=3 and busqueda.split():
                break
            else:
                print('la comuna debe tener minimo 3 carácteres.')
        for elemento in registros:
            if elemento["comuna"]==busqueda:
                with open (f'{elemento['comuna']}'+'.csv','w',newline='') as csvfile:
                    escritor = csv.writer(csvfile)
                    for elm in registros:
                        for x, y in elm.items():
                            escritor.writerow([x.upper()])
                            escritor.writerow([y])
                        escritor.writerow('\n')   