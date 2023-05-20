#           DIPLOMADO MACHINE LEARNING
#
#               jose miguel lagos
# 
#                actividad N°1
#
#  Corporación Unificada Nacional de Educación Superior  
#
#              20 de Mayo de 2023
#
import numpy as np
import json

file = open('data.json')
data = json.load(file)
file.close()

T = 7
# **** declarar vector *****
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
# lista para los dias de la semana
canSemana = []
# ref -> valor x und
ref = np.zeros((T,), dtype=int)
# arreglos por semana
lunes = np.zeros((T,), dtype=int)
martes = np.zeros((T,), dtype=int)
miercoles = np.zeros((T,), dtype=int)
jueves = np.zeros((T,), dtype=int)
viernes = np.zeros((T,), dtype=int)



# ingreo manual de valores x referencia
def referencias():
    for i in range(T):
        print(data['refPapa'][i]['nombre'])
        ref[i] = int(
            input("Digite valor de ventas de la referencia de papa frita " + data['refPapa'][i]['nombre']))
    return ref

# ingreo manual de valores por dias
def cantidadXDias():
    inxDia = 0
    for i in range(T):
        lunes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita " +
                  data['refPapa'][i]['nombre'] + " para el dia " + dias[inxDia]+" : "))
        inxDia += 1
        martes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita " +
                  data['refPapa'][i]['nombre'] + " para el dia " + dias[inxDia]+" : "))
        inxDia += 1
        miercoles[i] = int(
            input("Cantidad de ventas de la referencia de papa frita " +
                  data['refPapa'][i]['nombre'] + " para el dia " + dias[inxDia]+" : "))
        inxDia += 1
        jueves[i] = int(
            input("Cantidad de ventas de la referencia de papa frita " +
                  data['refPapa'][i]['nombre'] + " para el dia " + dias[inxDia]+" : "))
        inxDia += 1
        viernes[i] = int(
            input("Cantidad de ventas de la referencia de papa frita " +
                  data['refPapa'][i]['nombre'] + " para el dia " + dias[inxDia]+" : "))
        inxDia = 0

    return [lunes, martes, miercoles, jueves, viernes]

#cargar datos desde json 
def cantidadXDiasDatosJson():
    for i in range(T):
        lunes[i] = data['refPapa'][i]['ventas'][dias[0]]['cantidad']
        martes[i] = data['refPapa'][i]['ventas'][dias[1]]['cantidad']
        miercoles[i] = data['refPapa'][i]['ventas'][dias[2]]['cantidad']
        jueves[i] = data['refPapa'][i]['ventas'][dias[3]]['cantidad']
        viernes[i] = data['refPapa'][i]['ventas'][dias[4]]['cantidad']

    res = [lunes, martes, miercoles, jueves, viernes]
    print('Datos cargados desde json cantidad X Dias')
    print(res)

    return res

# calcula los totales
def costos(sumaSemana, precioXRef):
    total = np.zeros((T,), dtype=int)
    for i in range(T):
        total[i] = np.array(precioXRef[i]*sumaSemana[i])

    print('total ref x suma Semana')
    print(total)

    return total

# suma los valores po semana
def sumarSemana(semana):
    sumaSemana = np.zeros((T,), dtype=int)
    for i in range(len(semana)):
        sumaSemana = np.array(sumaSemana+semana[i])

    print('sumaSemana')
    print(sumaSemana)

    return sumaSemana

# 1. El valor de ventas por referencia y día 
# Tener en cuenta que las ventas son de una semana de lunes a
# viernes. 
def mostrarXRefXDia(sumaSemana, precioXRef):
    salidaDias = ' | referencia  | val x und | '
    arrPrint = []
    for i in range(len(dias)):
        salidaDias += dias[i]+' | '

    for j in range(T):
        salidaVal = ' |  '
        for i in range(len(dias)):
            salidaVal += str((sumaSemana[i][j]*precioXRef[j])) + '  | '
        arrPrint.append(salidaVal)

    print(salidaDias)
    for i in range(len(arrPrint)):
        print(' |    ' + data['refPapa'][i]['nombre'] +
              '    |   ' + str(precioXRef[i]) + '  ', arrPrint[i])

# 2. Determinar la venta mayor y la venta menor indicando
# la referencia 
def mostrarMaxMin(sumaSemana, total):

    minVenta = np.amin(total)
    minVentaIdx = np.argmin(total)

    maxVenta = np.amax(total)
    maxVentaIdx = np.argmax(total)

    print("La venta mayor de papas fritas es de " + data['refPapa'][maxVentaIdx]['nombre'] +
          ", es el valor de " + str(maxVenta) + " con " + str(sumaSemana[maxVentaIdx])+" Unds")
    print("La venta menor de papas fritas es de " + data['refPapa'][minVentaIdx]['nombre'] +
          ", es el valor de " + str(minVenta) + " con " + str(sumaSemana[minVentaIdx]) + " Unds")


def titulo():
    print("Empresa Margarita")


def salir():
    print("CHAO")

#cargar datos desde json 
def cargarDatosJsonRef():
    for i in range(T):
        ref[i] = int(data['refPapa'][i]['valorUnd'])

    print('Datos cargados desde json [ref]')
    print(ref)
    return ref

# valida si se cargan los datos o se ingresan manual
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
        canSemana = cantidadXDiasDatosJson()
        ref = cargarDatosJsonRef()
    else:
        ref = referencias()
        canSemana = cantidadXDias()
        print('Valores ingresados manualmente [ref]', ref)
        print('Valores ingresados manualmente cantidad X Dias', canSemana)

    totalSemana = sumarSemana(canSemana)
    totalGeneral = costos(totalSemana, ref)
    print('')
    print('************************************************************************')
    print('************************* Totales **************************************')
    print('************************************************************************')
    mostrarMaxMin(totalSemana, totalGeneral)
    print('************************************************************************')
    mostrarXRefXDia(canSemana, ref)
    salir()


# Bloque principal
main()
