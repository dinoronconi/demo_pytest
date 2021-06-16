from prediccion_math import  implemento_modelo
from operaciones import suma, resta

print('Suma : ', suma(21, 5))
print('Resta: ', resta(suma(21, 5), 5))

print('R2: ',implemento_modelo('StudentsPerformance.csv'))

