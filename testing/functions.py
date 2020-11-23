# Importar librerias
import pandas as pd 
import numpy as np
#from random import sample
from random_test import generate_data
#import prince
import joblib
import json


class processing_data():
    def __init__(self, data):
        self.data = data

    def transform_data(self):
        """transform_data : Transforma los datos numericos con el metodo PowerTransformer"""
        clf_reescalador = joblib.load('reescalador_v2.joblib')
        
        #print(self.data.columns)
        #print(self.data)
        self.data.set_index(['client_id', 'loan_id'], inplace=True)
        self.data[['arrears_days', 
                   'Monto Acumulado', 
                   #'Estrato Mínimo',# 
                   'Score Bureau Empresa', 
                   'Huellas de Consulta', 
                   #'Tiempo en el negocio'#,
                   'Edad empresarios',
                   'Número de accionistas','# Empleados', 
                   'Mujeres en cargos directivos']] = clf_reescalador.fit_transform(self.data[['arrears_days',
                                                                                               'Monto Acumulado', 
                                                                                               #'Estrato Mínimo',
                                                                                               'Score Bureau Empresa',
                                                                                               'Huellas de Consulta',
                                                                                               #'Tiempo en el negocio',
                                                                                               'Edad empresarios', 
                                                                                               'Número de accionistas', 
                                                                                               '# Empleados', 
                                                                                               'Mujeres en cargos directivos']])

        #print(self.data)
        self.data.reset_index(['client_id', 'loan_id'], inplace=True)
        return self.data

    def reduction_dim(self):
        """reduction: Reduce la dimensionalidad de los datos aplicando Analisis Factorial de Datos Mixtos(FAMD)"""
        self.data = self.transform_data()
        clf_reducir = joblib.load('famd_v2.joblib')
        self.data.drop(["client_id", "loan_id"], axis= 1, inplace=True)
        self.data ['state'] = self.data['state'].replace(to_replace="LATE", value="0")
        self.data ['state'] = self.data['state'].replace(to_replace="PAID", value="1")
        self.data ['state'] = self.data['state'].astype(object)
        
        transformada = clf_reducir.fit_transform(self.data )

        Y = transformada.to_numpy()
        principalDf_famd = pd.DataFrame(
            data=Y, columns=['principal component 1', 'principal component 2'])
        finalDf_Cat_famd = pd.concat(
            [principalDf_famd, self.data['state']], axis=1, ignore_index=True)

        self.data= finalDf_Cat_famd
        return self.data

def normalizar_to_df(json_):
    """Recibe en formato dict data para testear 
    
    Return: dataframe
    """
    json_ = (list(json_.values())[0][0:])
    json_= pd.DataFrame.from_dict(json_)

    #Eliminar index
    json_.reset_index(drop=True, inplace=True)
        #self.data.drop(['ID Cliente'], axis=1, inplace=True)
        #print(self.data)
    return json_