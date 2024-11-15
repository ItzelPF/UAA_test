from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        x= a/b
        if(x!=0):
            return x
        else:
            return 0
    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False.
        """
        for i in lista:
            if i % 2 != 0:
                return True
            else:
                return False

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        cont = 0
        for num in range (inicio, fin + 1):
            if num % 2 == 0:
                cont+=1
        return cont
 
    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        multiplos = []
        for i in lista:
            if i % multiplo == 0:
                multiplos.append(i)
                
        if multiplos:
            return max(multiplos)
        else: 
            print(None)

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        reves = palabra[::-1]
        if palabra == reves:
            return True
        else:
            return False

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(n):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        suma = 0
        for i in range (1, 2*n, 2): #2*n para generar más numero y llegar a los primeros n impares
            suma += i
        return suma

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        return len(lista) == len(set(lista))

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        resultado = 1 #1 porque si ponemos 0 la multiplicacion siempre será 0
        for i in range(1,numero+1):
            resultado *= i
        return resultado
        
    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        cont = 0
        for letra in cadena.lower():
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                cont += 1
        return cont

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        lista2 = list(set(lista)) #eliminar duplicados
        lista2.sort(reverse=True)
        if len(lista2) < 2:
            return None 
        else:
            return lista2[1]

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        fibonacci = [0, 1]
        while len(fibonacci) < n:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci[:n]
            
