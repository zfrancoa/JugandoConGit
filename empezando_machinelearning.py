# Tratamiento de datos
# ==============================================================================
from ast import For
import numpy as np
import pandas as pd
from tabulate import tabulate

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as ticker
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs
from sklearn.metrics import euclidean_distances
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge

from skopt.space import Real, Integer
from skopt.utils import use_named_args
from skopt import gp_minimize
from skopt.plots import plot_convergence

# Varios
# ==============================================================================
import multiprocessing
import random
from itertools import product
from fitter import Fitter, get_common_distributions
# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')



#OBTENEMOS LOS DATOS A TRATAR,El set de datos SaratogaHouses del paquete mosaicData de R contiene información sobre el precio de 1728 viviendas situadas en Saratoga County, New York, USA en el año 2006. Además del precio, incluye 15 variables adicionales:
url = "https://raw.githubusercontent.com/JoaquinAmatRodrigo/Estadistica-machine-learning-python/master/data/SaratogaHouses.csv"

#pd.read_csv: Lee un archivo de valores separados por comas (csv) en DataFrame.
#esta funcion tiene muchos atributos, el primero es el path al archivo
#pd. indica de que libreria es la funcion read_csv, pd significa pandas.
#el atributo sep creo que trata de que caracter es el que separa los distintos datos en el archivo cargado
#esta funcion devuelve: Un archivo de valores separados por comas (csv) se devuelve como una estructura de datos bidimensional con ejes etiquetados.
datos = pd.read_csv(url, sep=",")

# Se renombran las columnas para que sean más descriptivas
#El atributo Pandas DataFrame.columns devuelve las etiquetas de columna del marco de datos dado
#
datos.columns = ["precio", "metros_totales", "antiguedad", "precio_terreno",
                "metros_habitables", "universitarios", "dormitorios", 
                "chimenea", "banyos", "habitaciones", "calefaccion",
                "consumo_calefacion", "desague", "vistas_lago",
                "nueva_construccion", "aire_acondicionado"]


#.head sintaxis: pandas.DataFrame.head(n)
#Devuelve las primeras n filas que se le pasen como parametro.
#print(datos.head(4))                 



# Tipo de cada columna
# ==============================================================================
# En pandas, el tipo "object" hace referencia a strings
# datos.dtypes
#La dataframe.info() función Pandas se utiliza para obtener un resumen conciso del marco de datos. Resulta muy útil cuando se hace un análisis exploratorio de los datos
#datos.info()


# Dimensiones del dataset
# ==============================================================================
#print(datos.shape)


# Número de datos ausentes por variable
# ==============================================================================
#print(datos.isna().sum().sort_values())


#Variable respuesta:
#pyplot.subplotscrea una figura y una cuadrícula de subparcelas(grupos de ejes) con una sola llamada, al tiempo que proporciona un control razonable sobre cómo se crean las parcelas individuales. 
#el primer argumento indica cuantas filas tendremos, el segundo cuantas columnas, por lo tanto tendremos 3 subparcelas una arriba de la otra
#El tercer argumento en este caso representa el tamaño de la figura que se mostrara).
#Cuando se apila en una sola dirección(como es este caso), el axes resultado es una matriz numérica 1D que contiene la lista de ejes creados.
# fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 6))

# #.displot pertenece a la biblioteca seaborn
# #esta función esta obsoleta, cambiarla una ves que entendamos que hace
# #esta funcion trae varias dentro, como por ejemplo .rugplot() y .kdeplot()
# #Un Distplot o diagrama de distribución representa la variación en la distribución de datos. Seaborn Distplot representa la distribución general de variables de datos continuos.
# sns.distplot(
#     datos.precio,#datos observados
#     hist    = False,#True significa trazar un histograma
#     rug     = True,#True para dibujar un rugplot en el eje de soporte, rugplot que es una funcion, Esta función está destinada a complementar otros gráficos al mostrar la ubicación de las observaciones individuales de manera no obstructiva
#     color   = "blue",#Color para trazar todo menos la curva ajustada
#     kde_kws = {'shade': True, 'linewidth': 1},#Argumentos de palabras clave para kdeplot(), esta funcion Traza distribuciones univariadas o bivariadas utilizando la estimación de densidad kernel..
#     #shade:bool de sombra Alias ​​para fill. fillSe recomienda usar
#     ax      = axes[0]#ax: Si se proporciona, trace en este eje
# )
# axes[0].set_title("Distribución original", fontsize = 'medium')
# axes[0].set_xlabel('precio', fontsize='small') 
# axes[0].tick_params(labelsize = 6)

# sns.distplot(
#     np.sqrt(datos.precio),
#     hist    = False,
#     rug     = True,
#     color   = "blue",
#     kde_kws = {'shade': True, 'linewidth': 1},
#     ax      = axes[1]
# )
# axes[1].set_title("Transformación raíz cuadrada", fontsize = 'medium')
# axes[1].set_xlabel('sqrt(precio)', fontsize='small') 
# axes[1].tick_params(labelsize = 6)

# sns.distplot(
#     np.log(datos.precio),
#     hist    = False,
#     rug     = True,
#     color   = "blue",
#     kde_kws = {'shade': True, 'linewidth': 1},
#     ax      = axes[2]
# )
# axes[2].set_title("Transformación logarítmica", fontsize = 'medium')
# axes[2].set_xlabel('log(precio)', fontsize='small') 
# axes[2].tick_params(labelsize = 6)

# fig.tight_layout()#el .tight_layout() function se utiliza para ajustar las imagenes se les deja espacio entre titulo, etiquetas, etc, sino se hace eesto, una figura con otra se veran interceptadas.
# plt.show()#con esto mostramso la figura, La función show() en el módulo pyplot de la biblioteca matplotlib se usa para mostrar todas las figuras.



#Identificar a qué distribución se ajustan mejor los datos:
#Existen varias librerías en python que permiten identificar a qué distribución se ajustan mejor los datos, una de ellas es fitter. Esta librería permite ajustar cualquiera de las 80 distribuciones implementadas en scipy.
# distribuciones = ['cauchy', 'chi2', 'expon',  'exponpow', 'gamma',
#                   'norm', 'powerlaw', 'beta', 'logistic']

# #El paquete fiter proporciona una clase simple para identificar la distribución a partir de la cual se generan las muestras de datos.
# #el segundo parametro son las distribuciones que se usaran para el analisis y ver cual se ajusta mejor, si no se pasa este parametro se usaran las 80 distribuciónes con las que cuenta fitter.
# fitter = Fitter(datos.precio, distributions=distribuciones)
# #fit: Entrenamos nuestro modelo
# #fitter: es nuestro objeto transformador
# fitter.fit()
# #Elfitter.fitter.Fitter.summary()método muestra las primeras mejores distribuciones (en términos de ajuste).
# # Use .summary() la función para encontrar el resumen del Índice.
# print(fitter.summary(Nbest=10, plot=False))

# Variables numéricas
# ==============================================================================
#select_dtypes: Devuelve un subconjunto de las columnas de DataFrame en función de los tipos de columna
#parametro include: Una selección de dtypes o cadenas para incluiir.
# describe()método calcula y muestra estadísticas(significar, mediana, Desviación Estándar, mínimo, máximo, percentiles, etc)
# print(datos.select_dtypes(include=['float64', 'int']).describe())




# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
# fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(9, 5))
# #La función numpy.ndarray.flat() se utiliza como un iterador 1_D sobre matrices N-dimensionales.
# axes = axes.flat
# #El atributo Pandas DataFrame.columns devuelve las etiquetas de columna del marco de datos dado
# columnas_numeric = datos.select_dtypes(include=['float64', 'int']).columns
# #.drop():limine filas o columnas especificando nombres de etiquetas y ejes correspondientes, o especificando directamente nombres de índices o columnas
# #el primer parametro, Índice o etiquetas de columna para soltar(eliminar). Una tupla se usará como una sola etiqueta y no se tratará como una lista.
# columnas_numeric = columnas_numeric.drop('precio')

# #enumerate(): obtiene un contador(en que posicion del objeto iterable estamos) y el valor del iterable al mismo tiempo!
# for i, colum in enumerate(columnas_numeric):
#     #.hisplot(): Un histograma es una herramienta de visualización clásica que representa la distribución de una o más variables contando el número de observaciones que caen dentro de contenedores discretos.
#     sns.histplot(
#         data    = datos,#Estructura de datos de entrada
#         x       = colum,#Variable que especifica posicion en el eje x
#         stat    = "count",#Estadística agregada para calcular en cada contenedor, count: muestra el numero de observaciones en cada contenedor
#         kde     = True,#Si es Verdadero, calcule una estimación de densidad kernel para suavizar la distribución y mostrarla en el gráfico como (una o más) línea(s). Solo relevante con datos univariados.
#         color   = (list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],#Especificación de un solo color para cuando no se utiliza el mapeo de tonos. De lo contrario, la trama intentará conectarse con el ciclo de propiedades de matplotlib.
#         #rcParams: se utiliza para personalizar Matplotlib.
#         #axes.prop_cycle cambia el color de la traza, 
#         line_kws= {'linewidth': 2},#Parámetros que controlan la visualización de KDE
#         alpha   = 0.3,
#         ax      = axes[i]#Ejes preexistentes para la parcela.
#     )
#     axes[i].set_title(colum, fontsize = 7, fontweight = "bold")
#     axes[i].tick_params(labelsize = 6)
#     axes[i].set_xlabel("")
    
    
# fig.tight_layout()
# #con subplots_adjust:Ajustan los parámetros de diseño de la subparcela.
# #top: La posición del borde superior de las subtramas, como una fracción de la altura de la figura.
# plt.subplots_adjust(top = 0.9)
# fig.suptitle('Distribución variables numéricas', fontsize = 10, fontweight = "bold");
# plt.show()



#La variable chimenea, aunque es de tipo numérico, apenas toma unos pocos valores y la gran mayoría de observaciones pertenecen a solo dos de ellos. En casos como este, suele ser conveniente tratar la variable como cualitativa:
# Valores observados de chimenea
#La función Pandas Index.value_counts() devuelve un objeto que contiene recuentos de valores únicos. El objeto resultante estará en orden descendente, de modo que el primer elemento sea el que aparezca con más frecuencia. Excluye valores NA por defecto
# ==============================================================================
#print(datos.chimenea.value_counts())

# Se convierte la variable chimenea tipo string
#astype: para cambiar el tipo de dato de una columna
# ==============================================================================
datos.chimenea = datos.chimenea.astype("str")




# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(9, 5))
axes = axes.flat
columnas_numeric = datos.select_dtypes(include=['float64', 'int']).columns
columnas_numeric = columnas_numeric.drop('precio')

for i, colum in enumerate(columnas_numeric):
    #Grafique los datos y ajuste un modelo de regresión lineal.
    sns.regplot(
        #x e y: Variables de entrada. Si son cadenas, deben corresponder con los nombres de las columnas en data. Cuando se utilizan objetos pandas, los ejes se etiquetarán con el nombre de la serie.
        x           = datos[colum],
        y           = datos['precio'],
        #color: Color para aplicar a todos los elementos de la trama; serán reemplazados por colores pasados ​​en scatter_kwso line_kws.
        color       = "gray",
        marker      = '.',#Marcador que se usará para los glifos del diagrama de dispersión
        scatter_kws = {"alpha":0.4},#Argumentos de palabras clave adicionales para pasar a plt.scattery plt.plot
        line_kws    = {"color":"r","alpha":0.7},#Argumentos de palabras clave adicionales para pasar a plt.scattery plt.plot
        ax          = axes[i]#Objeto Axes sobre el que dibujar el gráfico; de lo contrario, utiliza los ejes actuales.
    )
    axes[i].set_title(f"precio vs {colum}", fontsize = 7, fontweight = "bold")
    #axes[i].ticklabel_format(style='sci', scilimits=(-4,4), axis='both')
    axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
    axes[i].xaxis.set_major_formatter(ticker.EngFormatter())
    axes[i].tick_params(labelsize = 6)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("")

# Se eliminan los axes vacíos
for i in [8]:
    fig.delaxes(axes[i])
    
fig.tight_layout()
plt.subplots_adjust(top=0.9)
fig.suptitle('Correlación con precio', fontsize = 10, fontweight = "bold");
plt.show()





















print("anano")