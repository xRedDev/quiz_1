'''
ESTE CÓDIGO FUE CREADO PARA LA MUESTRA Y CÁLCULO DE DATOS DE LA PRÁCTICA DE "MEDICIÓN DE LA GRAVEDAD"
DE LA MATERIA "PRINCIPIOS DE FÍSICA" - GRUPO 1.

PARTICIPANTES:
- Jair Enrique Armenta Rueda.
- Juan José Osorio Díaz.
- Sharith Celeste Castillo Mendoza.
'''

# librerias usadas (revisar el fichero requeriments y README.md para la descarga de estos mismos)
import matplotlib.pyplot as plt
import numpy as np

'''
GLOSARIO DE TÉRMINOS EMPLEADOS EN EL CÓDIGO
dt: delta t.
t: tiempos medidos en la práctica.
coeficientes: referencia a coeficientes del polinomio cuadrático.
fitted: ajustado / corregido.
RC: Regresión Cuadrática.
appreciation: apreciación de la toma de datos, este es proporcionado por el software usado: PhysicsSensor>Sonoscopio
'''


# =======-------- DATOS RECOPILADOS EN LA PRÁCTICA --------=======

dt = 0.01  # variación de la distancia (m)
distancias = np.arange(0.00, 0.15, dt)  # lista con todas las distancias desde 0.00 hasta 0.15 con paso dt
appreciation = 0.000033

t = np.array([
    0.000000,
    0.014510,
    0.025724,
    0.035955,
    0.045457,
    0.053970,
    0.062341,
    0.070081,
    0.077037,
    0.083765,
    0.090388,
    0.096740,
    0.102825,
    0.108798,
    0.114234,
])  # tiempos, cada uno en segundos

# =======-------- CÁLCULOS PARA LA REGRESIÓN CUADRÁTICA --------=======

# regresión cuadrática de la forma: y = ax^2 + bx + c
coeficientes, cov_matrix = np.polyfit(t, distancias, 2, cov=True)  # RC con matriz de covarianza
a, b, c = coeficientes  # obtenemos los coeficientes de forma individual

# cálculo de las incertidumbres (errores estándar) de los coeficientes
std_errors = np.sqrt(np.diag(cov_matrix))
inc_a, inc_b, inc_c = std_errors # obtenemos las incertidumbres individualmente

# se halla la gravedad experimental
g_exp = 2 * a

# ajuste de las distancias
fitted_distancias = a * t**2 + b * t + c


def calcular_error(
    valor_teorico: int | float = 9.78,  # este dato es g teorica
    valor_experimental: float = None,  # este dato es el error porcentual deseado
):
    '''
    `calcular_error()` devuelve el error respecto al dato teórico.\n
    ARGUMENTOS: \n
    `valor_teorico` por defecto es 9.78, ya que es el dato convencionalmente aceptado.\n
    `valor_experimental` es el dato obtenido experimentalmente que se desea comparar con el teórico.\n
    '''
    return abs((valor_teorico - valor_experimental) / valor_teorico) * 100


# =======-------- IMPRIMIMOS RESULTADOS EN LA CONSOLA/TERMINAL --------=======

print(f"Coeficientes de la regresión cuadrática ± la incertidumbre del dato:")
print(f"a (c_3) = {a:.8f} ± {inc_a:.8f}")
print(f"b (c_2) = {b:.8f} ± {inc_b:.8f}")
print(f"c (c_1) = {c:.8f} ± {inc_c:.8f}")
print(f"Gravedad experimental (g) = {g_exp:.4f} m/s^2")
print(f"El error calculado respecto al valor teórico es: {calcular_error(valor_experimental=g_exp):.4f}%")

# =======-------- GRAFICAR RESULTADOS Y VISUALIZACIÓN DE LOS DATOS --------=======

plt.figure(figsize=(8, 6))  # tamaño de la gráfica

plt.scatter(t, distancias, label="Datos experimentales", color="blue")  # colección de los datos originales

# graficar RC ajustado
plt.plot(t, fitted_distancias, label=f"Ajuste cuadrático: $y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}$", color="red")
plt.xlabel("Tiempo (s)")  # etiqueta para el eje `x`
plt.ylabel("Distancia (m)")  # etiqueta para el eje `y`

# titulo de la gráfica
plt.title("Regresión Cuadrática para la práctica de la Gravedad")

# datos booleanos
plt.legend()
plt.grid()
plt.show()
