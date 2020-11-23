# Importar librerias
import pandas as pd 
import numpy as np
from random_test import generate_data
from functions import processing_data, normalizar_to_df
import joblib
import json
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

def main():
    # Cargar modelo
    clf_model = joblib.load('modelo_ajustado_v2.joblib')
    # Datos a evaluar
    json_ = generate_data()
    
    json_ = json.loads(json_)
    
    data_normalizada = normalizar_to_df(json_)

    data_modelo = processing_data(data_normalizada)
    entrenar = data_modelo.reduction_dim().to_numpy()

    
    dict_result = {}
    for i in range(len(list(json_.values())[0][0:])):
        dictionary = (dict(list(json_.values())[0][i]))
    
        id_cliente = dict(list(json_.values())[0][i]).get('client_id')
        loan_id = dict(list(json_.values())[0][i]).get('loan_id')
        cluster_cliente = clf_model.predict(entrenar, categorical=[2])[i]
        dict_result[id_cliente] = {'loand_id': loan_id,'cluster': cluster_cliente}
    
    
    print(dict_result)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()