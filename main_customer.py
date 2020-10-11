# Importar librerias
import pandas as pd 
import numpy as np
from random import sample
import prince
import joblib

# Cargar modelo
clf_model = joblib.load('model_prueba.joblib')

# Cargar dato para generar data aleatoria
data = pd.read_csv('data_prueba.csv').iloc[:, 1:]

class processing_data():
    def __init__(self, data):
        self.data = data
        self.kproto = []
        self.clusters = []

    def transform_data(self):
        """transform_data : Transforma los datos numericos con el metodo PowerTransformer"""
        columns = ['client_id', 'loan_id']
        # Si el dataframe tiene las columnas borrarlo
        if all(item in list(self.data.columns) for item in columns):
            self.data.drop(columns, axis=1, inplace=True)

        # Transformar la data
        for c in self.data.select_dtypes(exclude='object').columns:
            pt = PowerTransformer()
            self.data[c] = pt.fit_transform(
                np.array(self.data[c]).reshape(-1, 1))
        return self.data

    def reduction_dim(self):
        """reduction: Reduce la dimensionalidad de los datos aplicando Analisis Factorial de Datos Mixtos(FAMD)"""

        self.data['state'] = self.data['state'].replace(
            ['LATE', 'PAID'], [0, 1])
        self.data['state'] = self.data['state'].astype(object)
        self.data.reset_index(drop=True, inplace=True)

        # Declarar metodo para aplicar FAMD
        famd = prince.FAMD(
            n_components=2,
            n_iter=3,
            copy=True,
            check_input=True,
            engine='auto',
            random_state=42)

        # Ajustar y transformar la dimensión aplicando FAMD
        famd = famd.fit(self.data)
        transformada = famd.transform(self.data)

        Y = transformada.to_numpy()
        principalDf_famd = pd.DataFrame(
            data=Y, columns=['principal component 1', 'principal component 2'])
        finalDf_Cat_famd = pd.concat(
            [principalDf_famd, self.data['state']], axis=1, ignore_index=True)

        self.data = finalDf_Cat_famd
        return self.data
    
numero = input("¿Cuántos clientes desea evaluar?")

# Generando un muestra aleatoria de 20 clientes
prueba= data.sample(int(numero))

#Procesar los datos de prueba
data_modelo = processing_data(prueba)
entrenar = data_modelo.reduction_dim().to_numpy()

print(f'clientes a evaluar {len(entrenar)}\n')
for i in range(len(entrenar)):
    print(f'Cliente #{i}\n\nLos datos del cliente son: {list(prueba.to_numpy()[i])}')
    print(f'Pertence al cluster: {clf_model.predict(entrenar, categorical=[2])[i]}\n')
