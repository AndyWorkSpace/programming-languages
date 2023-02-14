# Programa para Seleccionar números
# ***********************  MÓDULO PATRÓN  **************************
# Dado un conjunto de seleccionamos algunos valores
# Modulo Seleccionar
def Seleccionador(Modulo, *Elementos):
    for Elem in Elementos:
        if Modulo(Elem):
            print(Elem)
            
# *******************  PROGRAMA PRINCIPAL  **************************

# Mostrar las palabras que empiezen con 'I'
print("-"*60)
print("**********Palabras que empiezan con 'I'*********")
Seleccionador(lambda E : E>='I' and E<'J'
              , 'Ambidiestro', 'Ica', 'Muricielago'
              , 'Cajamarca','Inmigrante','Conservacionista')

# Mostrar palabras con una longitus mayor a 10
print("-"*60)
print("***Palabras que tienen una longitud mayor a 10***")
Seleccionador(lambda E : len(E)>=10,'Ambidiestro', 'Ica'
              , 'Muricielagos', 'Cajamarca','Concavo'
              ,'Conservacionista',"Otorrinolaringologo")
