from prediccion_math import  implemento_modelo
from operaciones import suma, resta

miSuma = suma(21, 5)
print('Suma : ', miSuma)
print('Resta: ', resta(suma(miSuma,8), 5))

print('R2: ',implemento_modelo('StudentsPerformance.csv', 0.33, 3, 8))



