# importando el modulo de regex de python
import re  



#Modificando el texto de entrada



# texto de entrada
becquer = """Podrá nublarse el sol eternamente; 
Podrá secarse en un instante el mar; 
Podrá romperse el eje de la tierra 
como un débil cristal. 
¡todo sucederá! Podrá la muerte 
cubrirme con su fúnebre crespón; 
Pero jamás en mí podrá apagarse 
la llama de tu amor."""



# patron para dividir donde no encuentre un caracter alfanumerico
patron = re.compile(r'\W+')

#split(): El cual divide el texto en una lista, realizando las divisiones del texto en cada lugar donde se cumple con la expresion regular
palabras = patron.split(becquer)
print(palabras[:10])  # 10 primeras palabras


# Utilizando la version no compilada de split.
print(re.split(r'\n', becquer))#Dividiendo por linea.


# Utilizando el tope de divisiones
print(patron.split(becquer, 5))



#Cambiando "Podrá" o "podra" por "Puede"
podra = re.compile(r'\b(P|p)odrá\b')
puede = podra.sub("Puede", becquer)
print(puede)



# Limitando el número de reemplazos
puede = podra.sub("Puede", becquer, 2)
print(puede)





# Utilizando la version no compilada de subn
print(re.subn(r'\b(P|p)odrá\b', "Puede", becquer))  # se realizaron 5 reemplazos


















































