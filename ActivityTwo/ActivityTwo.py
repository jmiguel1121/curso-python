#           DIPLOMADO MACHINE LEARNING
#
#               jose miguel lagos
# 
#                actividad N°2
#
#  Corporación Unificada Nacional de Educación Superior  
#
#              27 de Mayo de 2023
#
import json

file = open('data.json')
data = json.load(file)
file.close()
accion = ['TMR', 'compra', 'venta']


# imprime las divisas del archivo json y el index e el consecutivo de la
# divisa a ser Seleccionada
def imprimirDivisas():
    print('======================================================')
    print('============= Sistema de Cambio de Divisas ===========')
    print('======================================================')
    idx = 1
    for divisa in data['divisas']:
        print(str(idx) + '. ' + divisa['moneda'] + ' : ' + divisa['nombre'])
        idx = idx+1

    print('================= Divisas ============================')


def cacularDivisa(cantidad, idxDivisa, accion):
    divisa = data['divisas'][idxDivisa]['valor'][accion]
    res = cantidad / int(divisa)

    return round(res, 2)


def calcularGanaciaPerdida(valTMR, valCompra, valVenta):
    res = {"Ganancia comprador => ": round(valCompra-valTMR, 2),
           "Ganancia vendedor => ": round(valVenta-valTMR, 2)}

    return res


def validarSEleccionRango(ixd):
    return ixd < len(data['divisas'])


def procesoConvertidorDivisa(ixd):
    divisa = data['divisas'][ixd]
    print('******'+divisa['moneda']+'-'+divisa['nombre']+'******')
    valor = int(input('Por favor ingrese la cantidad: '))
    valTMR = cacularDivisa(valor, ixd, accion[0])
    valCompra = cacularDivisa(valor, ixd, accion[1])
    valVenta = cacularDivisa(valor, ixd, accion[2])
    informe = calcularGanaciaPerdida(valTMR, valCompra, valVenta)
    valConverciones = (valTMR, valCompra, valVenta)
    print('***************** Informe ******************************')
    for i in range(len(accion)):
        print(' * ' + str(accion[i]) + ' -> '+str(valConverciones[i]))
    print('--------------------------------------------------------')
    print(informe)
    print('********************************************************')


def validaContinuar():
    res = ''
    while res == '':
        print('***************** Señor Usuario *********************')
        continuar = input('!Desea Continuar Si=s / No=n : ')
        if continuar == 's' or continuar == 'n':
            res = continuar

    return res != 's'


def main():
    salir = False
    while not salir:
        imprimirDivisas()
        ixd = int(input('Seleccione la Divisa que desea convertir: '))
        ixd = ixd-1
        if validarSEleccionRango(ixd):
            procesoConvertidorDivisa(ixd)
        salir = validaContinuar()
    
    print('============ !Adios ======================================')    

main()
