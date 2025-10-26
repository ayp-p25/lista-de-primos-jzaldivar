lista_primos = []
entrada = int(input("Escriba el número del cual quieres conocer la
lista"))
# Proceso
for num in range(1,entrada+1):
 es_primo = True
 for i in range(2,num):
 if num % i == 0:
 es_primo = False
 break
 if es_primo:
 lista_primos.append (num)
# Salidas
print("tu lista de número primos menores que", entrada, "es ", lista_primos)

