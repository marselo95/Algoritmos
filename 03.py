def menu():
    print("""
    
    Que desea hacer?
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Potencia
    6) Modulo
    7) Comparar
    8) Valor absoluto
    9) Salir
    """)


def calculadora():

    while True:
        menu()

        opc = input('Introduce el numero de la opcion: ')
        n1 = int(input('Introduce el primer numero: '))
        n2 = int(input('Introduce el segundo numero: '))

        if n1 is int:

            if opc == '1':

                print('El resultado es: ', n1+n2)

            elif opc == '2':

                print('El resultado es: ', n1-n2)

            elif opc == '3':

                print('El resultado es: ', n1*n2)

            elif opc == '4':

                try:
                    r = n1/n2
                    print('El resultado es: ', r)
                except ZeroDivisionError:
                    print('No es posible dividir entre 0')

            elif opc == '5':
                n1 = int(input('Introduce el numero base: '))
                n2 = int(input('Introduce el numero exponente: '))
                print('El resultado es: ', n1**n2)

            elif opc == '6':

                print('El resultado es: ', n1 % n2)

            elif opc == '7':

                if n1 > n2:
                    print('El numero {} es mayor que {}'.format(n1, n2))
                elif n1 < n2:
                    print('El numero {} es menor que {}'.format(n1, n2))
                else:
                    print('Los numeros son iguales')

            elif opc == '8':

                r = abs(n1)
                print('El valor absoluto de {} es {}'.format(n1, r))
            elif opc == '9':
                print('Hasta luego!')
                break
            else:
                print("Opcion desconocida, por favor intentalo de nuevo")
        else:
            print("Por favor ingresa un valor numerico")


calculadora()
