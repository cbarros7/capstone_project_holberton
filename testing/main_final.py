# Importar librerias
import pandas as pd 
import numpy as np
from random import sample
from random_test import ran,randomizer,generate_data
import prince
import joblib
import json

# Cargar modelo
clf_model = joblib.load('model_prueba.joblib')


def normalizar_to_df(json_):
    """Recibe en formato dict data para testear 
    
    Return: dataframe
    """
    # Convierte dictionario de los valores de prueba en una lista
    test_transform = (list(json_.values())[0][0:])
    
    # Convierte la lista en un nuevo diccionario
    newdict={}
    for k,v in [(key,d[key]) for d in test_transform for key in d]:
        if k not in newdict:
            newdict[k]=[v]
        else:
            newdict[k].append(v)
    
    # Serializa el nuevo diccionario a json 
    json_object = json.dumps(newdict, indent = 4)
    
    # Deserialización
    data = json.loads(json_object)
    
    #Convetir a dataframe
    train = pd.DataFrame.from_dict(data, orient='index', columns=['datos'])
    #Eliminar index
    train.reset_index(drop=True, inplace=True)
    return train['datos'].apply(pd.Series)

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
        #print(finalDf_Cat_famd.isnull().sum())
        self.data = finalDf_Cat_famd
        return self.data

# Datos a evaluar
json_ = generate_data()

json_ = json.loads(json_)
normalizar_json = normalizar_to_df(json_)
#print(normalizar_json)

#Procesar los datos de prueba
data_modelo = processing_data(normalizar_json)
entrenar = data_modelo.reduction_dim().to_numpy()
#entrenar = entrenar.replace([np.inf, -np.inf], np.nan)
#entrenar = entrenar.to_numpy()
#print(type(entrenar))

print(f'clientes a evaluar {len(entrenar)}\n')
for i in range(len(entrenar)):
    #print(f'Cliente #{i}\n\nLos datos del cliente son: {list(prueba.to_numpy()[i])}')
    print(f'Pertence al cluster: {clf_model.predict(entrenar, categorical=[2])[i]}\n')
