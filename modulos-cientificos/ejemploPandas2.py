#panadas es una biblioteca que nos permite el manejo de información mediante tablas
# su principal uso es el analisis de datos
#pip install pandas
#Series
#DataFrames
#Panel

import pandas as pd #pd alias estar

serie = pd.Series(['Ronaldo','Messi','Puyol','Cuau','Ramos'],index=[7,10,5,11,4]) 
print("jugadores: \n %s"%serie)


serie = pd.read_excel("Doc1.xlsx")

print(serie)