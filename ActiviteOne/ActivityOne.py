# import library numpy
import numpy as np
import json

file = open('data.json')
data = json.load(file)
file.close()

# declarar vector
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
can, ref, total, dias = [], [], [], []
lunes, martes, miercoles, jueves, viernes = [], [], [], [], []
T = 7


def test():
    # arr= np.array([can],[ref],[total])
    print('arr')
    print(data['refPapa'])


def inicializar():
    for i in range(T):
        lunes.append(0)
        martes.append(0)
        miercoles.append(0)
        jueves.append(0)
        viernes.append(0)
        ref.append(0)
        print(can)


def inicializarTotal():
    for i in range(T):
        total.append(0)


def referencias():
    for i in range(T):
        ref[i] = int(
            input("Digite valor de ventas de la referencia de papa frita ", data['refPapa'][i]))
    return ref


def cantidadXDias():
    inxDia = 0
    for i in range(T):
        lunes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita",
                  data['refPapa'][i], "para el dia ", dias[inxDia]))
        inxDia += 1
        martes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita",
                  data['refPapa'][i], "para el dia ", dias[inxDia]))
        inxDia += 1
        miercoles[i] = int(
            input("Cantidad de ventas de la referencia de papa frita",
                  data['refPapa'][i], "para el dia ", dias[inxDia]))
        inxDia += 1
        jueves[i] = int(
            input("Cantidad de ventas de la referencia de papa frita",
                  data['refPapa'][i], "para el dia ", dias[inxDia]))
        inxDia += 1
        viernes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita",
                  data['refPapa'][i], "para el dia ", dias[inxDia]))
        inxDia = 0

    return ref


def costos(can, ref):
    for i in range(T):
        total[i] = can[i]*ref[i]

    print('total')
    print(total)
    return total


def mostrar(can, ref, total):
    tgc = 0
    tgv = 0
    # print(can)
    # print(ref)
    # print(total)

    for i in range(T):
        tgc = tgc+can[i]

    for i in range(T):
        tgv = tgv+total[i]

    print("Las ventas totales en unidades de papas fritas es de", tgc)
    print("Las ventas totales en dinero de papas fritas es de", tgv)


def titulo():
    print("Empresa Margarita")


def salir():
    print("CHAO")


def cargarDatosJsonRef():
    for papa in data['refPapa']:
        # print(papa['codigo'])
        ref.append(int(papa['valorUnd']))

    print('Datos cargados desde json [ref]')
    print(ref)
    return ref


def cargarDatosJsonCan():
    for papa in data['refPapa']:
       # print(papa['valorUnd'])
        can.append(int(papa['cantVend']))

    print('Datos cargados desde json [can]')
    print(can)
    return can


def validarCargaDatos():
    continuar = False
    res = ''
    while continuar is False:
        print("Desea cargar automaticamentos los datos desde el archivo")
        res = input("Si=s / No=n : ")
        continuar = res == 's' or res == 'n'

    return res == 's'


def main():
    titulo()
    cargarDatos = validarCargaDatos()
    if (cargarDatos):
        can = cargarDatosJsonCan()
        ref = cargarDatosJsonRef()
        inicializarTotal()
    else:
        inicializar()
        inicializarTotal()
        can = captura()
        ref = referencias()

    # test()
    total = costos(can, ref)
    mostrar(can, ref, total)
    salir()


# Bloque principal
main()
