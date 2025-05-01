def invertir_array(array_original):
  array_invertido = array_original[::-1]
  return array_invertido

try:
  cantidad_elementos = int(input("ingrese la cantidad de elementos del array: "))
  array = []
  for i in range(cantidad_elementos):
    valor = input(f"ingrese el valor del elemento {i + 1}: ")
    array.append(valor)

  array_invertido = invertir_array(array)

  print("\na4rray original:", array)
  print("array invertido:", array_invertido)

except ValueError:
  print("por favor ingresar un numero entero valido.")