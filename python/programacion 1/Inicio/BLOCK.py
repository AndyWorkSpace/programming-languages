
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Notas=[]
for subject in subjects:
    Nota=eval(input('Ingrese nota de '+str(subject)+':'))
    Notas.append(Nota)
print(subjects,Notas)

for i in Notas:
    if i>=13.5:
        del i
print(Notas)
