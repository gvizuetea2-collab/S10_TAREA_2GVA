# '''Ejercicio 1. Sistema de Estudiantes'''
class Estudiante:
    def __init__(self,nombre,edad,carrera,promedio):
        self.nombre=nombre
        self.edad=edad
        self.carrera=carrera
        self.promedio=promedio
    def __str__(self):
        return f'estudiante: {self.nombre}, edad: {self.edad}, carrera: {self.carrera}, promedio:{self.promedio}'
    def determinar_si_aprobo(self):
        if self.promedio>=7:
            print('el estudiante si aprueba')
        else:
            print('el estudiante no cumple con los requisitos')
    def actualizar_promedio(self,nueva_nota):
        self.promedio=nueva_nota
est1=Estudiante("Xavier",19,"ing en software",4)
print(est1)
est1.determinar_si_aprobo()
est1.actualizar_promedio(9)
print(est1)
est1.determinar_si_aprobo()

''' Ejercicio 2. Cuenta Bancaria '''
class CuentaBancaria:
    def __init__(self,titular,numb_cuenta,saldo):
        self.titular=titular
        self.numb_cuenta=numb_cuenta
        self.saldo=saldo
    def __str__(self):
        return f'titular: {self.titular}, numero de cuenta: {self.numb_cuenta}, Saldo: {self.saldo}'
    def depositar(self,monto_dep):
        self.saldo+=monto_dep
    def retirar(self,monto_ret):
        if self.saldo>=monto_ret:
            self.saldo-=monto_ret
        else:
            print("fondos insuficientes")
    def consultar_saldo(self):
        return self.saldo
cuent1=CuentaBancaria("Xavier","0957104490",90)
print(cuent1)
cuent1.depositar(500)
cuent1.consultar_saldo()
cuent1.retirar(90)
print(cuent1)

'''Ejercicio 3. Inventario de Productos'''
class Producto:
    def __init__(self,codigo,nombre,precio,stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def comprar(self,venta):
        if self.stock>=venta:
            self.stock-=venta
        else:
            print("la cantidad supera el stock")
    def reabastecer(self,cant_producto):
        self.stock+=cant_producto
    def calcular_valor_inventario(self):
        return self.precio * self.stock
prod1=Producto("001","cocacola",0.50,4)
total=prod1.calcular_valor_inventario()
print(total)

''' Ejercicio 4. Sistema de Reservas '''


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = True

    def ocupar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print("Habitación reservada correctamente.")
        else:
            print("La habitación ya está ocupada, no se puede reservar.")

    def liberar(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print("Habitación liberada correctamente.")
        else:
            print("La habitación ya está disponible.")

    def mostrar_info(self):
        if self.disponibilidad:
            estado = "Disponible"
        else:
            estado = "Ocupada"
        return f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}"


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def reservar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.ocupar()
                return
        print("Habitación no encontrada")

    def liberar_habitacion(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.liberar()
                return
        print("Habitación no encontrada")

    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.disponibilidad:
                print(habitacion.mostrar_info())

    def mostrar_habitaciones_ocupadas(self):
        print("Habitaciones reservadas:")
        for habitacion in self.habitaciones:
            if not habitacion.disponibilidad:
                print(habitacion.mostrar_info())


hotel = Hotel("Hotel Ecuador")

h1 = Habitacion(101, "Individual", 50)
h2 = Habitacion(102, "Doble", 80)
h3 = Habitacion(103, "Suite", 150)

hotel.agregar_habitacion(h1)
hotel.agregar_habitacion(h2)
hotel.agregar_habitacion(h3)

hotel.mostrar_habitaciones_disponibles()

hotel.reservar_habitacion(102)

hotel.mostrar_habitaciones_disponibles()

hotel.mostrar_habitaciones_ocupadas()

hotel.liberar_habitacion(102)

hotel.mostrar_habitaciones_disponibles()

''' Ejercicio 5. Herencia de Animales '''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print(self.nombre, "dice: Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print(self.nombre, "dice: Miau miau")

class Ave(Animal):
    def hacer_sonido(self):
        print(self.nombre, "dice: Pío pío")

animales = [
    Perro("Firulais"),
    Gato("Tom"),
    Ave("Piolín")
]
for animal in animales:
    animal.hacer_sonido()

''' Ejercicio 6. Sistema de Figuras Geométricas '''
class Figura:
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

figuras = [
    Rectangulo(5, 4),
    Circulo(3),
    Triangulo(3, 4, 5, 4, 3)
]


for figura in figuras:
    print("Área:", figura.calcular_area())
    print("Perímetro:", figura.calcular_perimetro())
    print("----------------------")
''' Ejercicio 7. Gestión de Universidad '''


class Persona:
    def __init__(self, nombre, edad, num_cedula):
        self.nombre = nombre
        self.edad = edad
        self.num_cedula = num_cedula

    def cumplir_anios(self):
        self.edad += 1

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Cédula: {self.num_cedula}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, num_cedula, carrera, semestre, promedio):
        super().__init__(nombre, edad, num_cedula)
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.rubros_pendientes = 0

    def cambiar_de_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def pasar_semestre(self):
        self.semestre += 1

    def actualizar_promedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio

    def aumentar_rubros(self, valor):
        self.rubros_pendientes += valor

    def pagar_rubros(self, pago):
        if self.rubros_pendientes == pago:
            self.rubros_pendientes = 0
            return 0
        elif self.rubros_pendientes < pago:
            vuelto = pago - self.rubros_pendientes
            self.rubros_pendientes = 0
            return vuelto
        else:
            a_deber = self.rubros_pendientes - pago
            self.rubros_pendientes = a_deber
            return a_deber

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Cédula: {self.num_cedula}, Carrera: {self.carrera}, Semestre: {self.semestre}, Promedio: {self.promedio}, Rubros pendientes: ${self.rubros_pendientes}"


class Profesor(Persona):
    def __init__(self, nombre, edad, num_cedula, materia, sueldo, facultad):
        super().__init__(nombre, edad, num_cedula)
        self.materia = materia
        self.sueldo = sueldo
        self.facultad = facultad

    def cambiar_de_materia(self, materia_nueva):
        self.materia = materia_nueva

    def actualizar_sueldo(self, nuevo_sueldo):
        self.sueldo = nuevo_sueldo

    def descuento_por_multa(self, descuento):
        self.sueldo -= descuento

    def __str__(self):
        return f"Profesor: {self.nombre}, Edad: {self.edad}, Cédula: {self.num_cedula}, Materia: {self.materia}, Facultad: {self.facultad}, Sueldo: ${self.sueldo}"


est1 = Estudiante("Jade", 20, "0951234567", "Ingeniería en Software", 3, 8.9)
prof1 = Profesor("Jhon", 45, "0912345678", "Estructura de Datos", 1800, "UNEMI")

print(est1)
print(prof1)

print("--------------------------")

est1.cumplir_anios()
prof1.cumplir_anios()

est1.pasar_semestre()
est1.actualizar_promedio(9.4)
est1.aumentar_rubros(150)
print("Rubros pendientes:", est1.rubros_pendientes)

deuda = est1.pagar_rubros(100)
print("Saldo pendiente:", deuda)

prof1.cambiar_de_materia("Base de Datos")
prof1.actualizar_sueldo(2000)
prof1.descuento_por_multa(100)

print("--------------------------")

print(est1)
print(prof1)

''' Ejercicio 8. Sistema de Pedidos '''
class Pedido:
    def __init__(self,id_pedido):
        self.id_pedido = id_pedido
        self.productos=[]
        self.total=0
        self.subtotal=0
        self.total_IVA=0
        self.IVA=0.15
    def agregar_productos(self,producto):
        self.productos.append(producto)
    def eliminar_producto(self,id_producto):
        for producto in self.productos:
            if producto.id_producto==id_producto:
                self.productos.remove(producto)
                return "Producto eliminado"
        return "producto inexistente"
    def calcular_subtotal(self):
        self.subtotal = 0
        for producto in self.productos:
            self.subtotal+=producto.precio
    def calcular_iva(self):
        self.total_IVA=self.subtotal*self.IVA
    def calcular_total(self):
        self.total=self.subtotal+self.total_IVA
    def mostrar_inf(self):
        pedido= f'subtotal: {self.subtotal}, total IVA: {self.total_IVA}, total: {self.total}, productos:\n'
        for producto in self.productos:
            pedido+=producto.inf_producto()+"\n"
        return pedido
class Producto:
    def __init__(self,id_producto,nombre,precio):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
    def inf_producto(self):
        return f'id: {self.id_producto}, nombre: {self.nombre}, precio:{self.precio}'
class Cliente:
    def __init__(self,nombre,numb_cedula):
        self.nombre=nombre
        self.numb_cedula=numb_cedula
        self.pedidos=[]
    def agregar_pedido(self,pedido):
        self.pedidos.append(pedido)
    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido.mostrar_inf())

# lo dejo comentado por qué si es algo grandecito xd
prod1 = Producto(1, "Laptop", 800)
prod2 = Producto(2, "Mouse", 25)
prod3 = Producto(3, "Teclado", 40)

# Crear pedido
pedido1 = Pedido(1001)

# Agregar productos al pedido
pedido1.agregar_productos(prod1)
pedido1.agregar_productos(prod2)
pedido1.agregar_productos(prod3)

# Calcular valores del pedido
pedido1.calcular_subtotal()
pedido1.calcular_iva()
pedido1.calcular_total()

# Crear cliente
cliente1 = Cliente("Eduardo Alvarez", "0951234567")

# Asignar pedido al cliente
cliente1.agregar_pedido(pedido1)

# Mostrar información del pedido
cliente1.mostrar_pedidos()
print("------------------------")

# Probar eliminar producto
print(pedido1.eliminar_producto(2))

# Recalcular después de eliminar
pedido1.calcular_subtotal()
pedido1.calcular_iva()
pedido1.calcular_total()

# Mostrar pedido actualizado
print(pedido1.mostrar_inf())

''' Ejercicio 9. Búsqueda en Lista '''
def buscar(lista,valor):
    for elemento in lista:
        if elemento==valor:
            return True
    return False
'''mejor caso:
si el valor buscado esta en la primera posición de la lista, en ese caso solo se haría una comparación
peor caso:
si el valor buscado noo esta en la lista o esta en la ultima posición, se recorre cada posición de la lista hasta llegar a dico valor
complejidad Big O:
O(n)
'''


''' Ejercicio 10. Comparación de Algoritmos '''
# a)
for i in range(n):
    print(i)
''' T(n) = n
Complejidad: O(n) '''
# b)
for i in range(n):
    for j in range(n):
        print(i, j)
''' T(n) = n²
Complejidad: O(n²) '''
# c)
i = n
while i > 1:
    i = i // 2
''' T(n) = log₂(n)
Complejidad: O(log n) '''
# orden de algoritmos según su eficiencia:
# c)
i = n
while i > 1:
    i = i // 2
# a)
for i in range(n):
    print(i)
# b)
for i in range(n):
    for j in range(n):
        print(i, j)
''' justificación:
el logaritmo crece muchísimo más lento que cualquier función lineal o cuadrática,
 porque cada iteración descarta la mitad del problema en lugar de avanzar de a uno 
 O(logn) < O(n) < O(n2)'''



''' Ejercicio 11. Análisis de Complejidad de un Algoritmo
Analice el siguiente algoritmo y determine su complejidad temporal '''
def analizar(lista): #1 marcas temporales

    n = len(lista)#1
    total = 0#1

    # Primer recorrido
    for i in range(n):#n
        total += lista[i]#1

    # Segundo recorrido
    for i in range(n):#n
        for j in range(i, n):#n
            if lista[j] % 2 == 0:#1
                total += lista[j]#1

    # Tercer recorrido
    k = n#1
    while k > 1:#logn
        total += k
        k //= 2

    # Cuarto recorrido
    for i in range(n):#n
        for j in range(5):#1
            total += i + j#1

    return total#1

''' t(n): 1(1+1+n(n(1(1)))+1+logn+n(1(1)) 
aqui una version mas formalizada de la funcion:
T(n)=1+1+n+(n(n+1))/2+log2n+5n+1
Big O:  O(n²)'''