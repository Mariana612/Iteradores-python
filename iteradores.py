# la keyword YIELD cambia una funcion normal a un generador (generator). 
# Los generadores en vez de guardar toda la informacion a la vez van generado los valores a demanda
# ejemplo:

"""Un generador es una función especial que utiliza la palabra clave yield.
Cuando una función contiene yield, en lugar de devolver el valor y terminar,
 se pausa en el yield y conserva su estado. Cuando la siguiente llamada al
 generador se hace (usando next() o dentro de un bucle), 
el generador reanuda su ejecución desde el último yield, produciendo el siguiente valor."""

def itere(): 
    yield 1
    yield 2
    yield 3

# gen = itere()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for i in itere():
#     print(i)
# itere()

def rango(i,n):
    while i <= n:
        yield i
        i += 1
    
for i in rango(2,4):
    print(i)

def rangorec(i,n):
    if i <= n:
        yield i
        yield from rangorec(i+1, n)

for i in rangorec(2,4):
    print(i)
