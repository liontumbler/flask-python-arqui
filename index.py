import psutil
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Uso de CPU: {cpu_usage}%")

import GPUtil
gpus = GPUtil.getGPUs()
print(gpus)
#gpu = gpus[0]
#print(gpu)
"""
for gpu in gpus:
    print(f"GPU: {gpu.name}")
    print(f"Uso de GPU: {gpu.load * 100}%")
    print(f"Memoria libre: {gpu.memoryFree}MB")
    print(f"Memoria utilizada: {gpu.memoryUsed}MB")
    print(f"Memoria total: {gpu.memoryTotal}MB")
    print(f"Temperatura: {gpu.temperature} C")
"""




import math

def find_integer_n(base, subred):
    while True:
        n = math.log(subred) / math.log(base)
        if n.is_integer():
            return subred, int(n)
        subred += 1

def find_maskara(bit_opteto):
    clases = ['A', 'B', 'C', 'D', 'E']
    Maskaras = [8, 16, 24, 27, 28]
    clases_ip = [0, 128, 192, 224, 240] #A, B, C, D, E

    for i in range(len(clases_ip)):
        if bit_opteto >= clases_ip[i] and bit_opteto < clases_ip[i +1]:
            return clases[i], Maskaras[i], i

cons_ip = 256
base_dos = 2

clase = ''
maskara = 0
index_mascara = 0

ip_spliteada = []
while True:
    try:
        ip = input("Introduce un número IPv4 de la red a subnetear eje '192.168.1.1': ")
        partes = ip.split('.')
        tamaño = len(partes)
        if tamaño == 4:
            for i in range(tamaño):
                if partes[i].isdigit():
                    octeto_entero = int(partes[i])
                    ip_spliteada.append(octeto_entero)
                    if i == 0:
                        clase, maskara, index_mascara = find_maskara(octeto_entero)
                    
                    """if index_mascara +1 == i:
                        numero_binario = bin((256 - octeto_entero))[2:]
                        cantidad_de_unos = numero_binario.count('1')
                        maskara = maskara + cantidad_de_unos"""
                else:
                    break

        if len(ip_spliteada) == 4:
            break
        else:
            print("ocurrio un error en la digitacion. Inténtalo de nuevo.")
    except ValueError:
        print("puede que el valor este vacio. Inténtalo de nuevo.")


while True:
    try:
        confirmacion_cantidad = input("quieres que las sunredes, tengan la misma cantidad de equipos s/n:")
        break
    except ValueError:
        print("Eso no es un número entero válido. Inténtalo de nuevo.")








print("misma cantidad", confirmacion_cantidad, clase, maskara, index_mascara)
if confirmacion_cantidad == 's':
    print("ip igual cantidad")
else:
    while True:
        try:
            cadena_numeros = input("ingresa la cantidad que necesitas por host separado por ',' Eje: 12,120,4: para terminar teclea enter:")
            
            array_numeros = [int(num) for num in cadena_numeros.split(',')]

            numeros_ordenados = sorted(array_numeros, reverse=True)
            
            break
        except ValueError:
            print("Eso no es un número entero válido. Inténtalo de nuevo.")
    
    ip_real = ip_spliteada[:]
    num_bit_disponibles = 32 - maskara
    print(f"| IP: {ip} | Maskara actual: {maskara} | Hosts: {numeros_ordenados} |")
    print("| NO | Maskara | Direc-red | broadcast | rango |")
    for i in range(len(numeros_ordenados)):
        if num_bit_disponibles > 0:

            nueva_subred, n = find_integer_n(base_dos, (numeros_ordenados[i] +2))

            m = num_bit_disponibles -n

            nueva_maskara = maskara + m

            numero_binario = '1' * n

            broadcast = [ip_real[3], ip_real[2], ip_real[1], ip_real[0]]
            
            partes_de_bits = [numero_binario[i:i+8] for i in range(0, len(numero_binario), 8)]
            for e in range(len(partes_de_bits)):   
                broadcast[e] = broadcast[e] + int(partes_de_bits[e], 2)

            broadcast_real = broadcast[::-1]

            rango_inicial = ip_real[:]
            if rango_inicial[3] +1 <= 255:
                rango_inicial[3] = rango_inicial[3] +1
            elif rango_inicial[2] +1 <= 255:
                rango_inicial[2] = rango_inicial[2] +1
            elif rango_inicial[1] +1 <= 255:
                rango_inicial[1] = rango_inicial[1] +1
            elif rango_inicial[0] +1 <= 255:
                rango_inicial[0] = rango_inicial[0] +1

            rango_final = broadcast_real[:]
            if rango_final[3] -1 >= 0:
                rango_final[3] = rango_final[3] -1
            elif rango_final[2] -1 >= 0:
                rango_final[2] = rango_final[2] -1
            elif rango_final[1] -1 >= 0:
                rango_final[1] = rango_final[1] -1
            elif rango_final[0] -1 >= 0:
                rango_final[0] = rango_final[0] -1
            
            print(f"| {(i+1)} Host de {numeros_ordenados[i]} | {nueva_maskara} | {ip_real} | {broadcast_real} | {rango_inicial} - {rango_final} |")

            num_bit_disponibles = num_bit_disponibles -m

            maskara = nueva_maskara 

            if (broadcast_real[3] + 1) <= 255:
                ip_real[3] = (broadcast_real[3] + 1)
            elif (broadcast_real[2] + 1) <= 255:
                ip_real[2] = (broadcast_real[2] + 1)
            elif (broadcast_real[1] + 1) <= 255:
                ip_real[1] = (broadcast_real[1] + 1)
            elif (broadcast_real[0] + 1) <= 255:
                ip_real[0] = (broadcast_real[0] + 1)
        else:
            print('No hay bits suficientes para la operacion intenta con menos cantidad o una clase que permita dicha cantidad')





















from flask import Flask
from src.routes.routes import init_routes

app = Flask(__name__)

init_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)