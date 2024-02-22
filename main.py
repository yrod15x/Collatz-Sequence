def registrar_solo_enteros()->int:
    """Verifica que la entrada de datos sea un numero entero no igual a 0"""
    while True:
        try:
            num = int(input("Ingrese un numero entero >> "))
            if num != 0:
                break
            else:
                print('El numero debe ser mayor a 0!')
                continue
        except ValueError:
            print('El dato no es un numero entero valido!')
    return num

def extraer_sec_collatz(num:int)->list:
    """Regresa una lista con la secuencia de Collatz del parametro num"""
    list_secuencia = []
    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num //=2
        else:
            num = num * 3 + 1
        list_secuencia.append(num)
    return list_secuencia

def mostrar_sec_collatz(list_num:list, num:int)->None:
    """Imprime la secuencia de Collatz del parametro num"""
    print(f"La secuencia de Collatz del numero {num} es: ")
    for n in list_num:
        print(n, end=" ")

numero = registrar_solo_enteros()
mostrar_sec_collatz(extraer_sec_collatz(numero),numero)