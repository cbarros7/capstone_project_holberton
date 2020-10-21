#!/usr/bin/python3
import random
import json

def ran(list):
    return(list[random.randint(0, len(list) - 1)])

def randomizer():
    # variables numéricas.
    # ------------------------------------------------
    clientId = random.randint(1, 1000)
    loanId = random.randint(1, 1000)
    arrearDays = random.randint(0, 258)
    montoAcumulado = random.randint(30000000, 1299370581)
    scoreBureauEmpresa = random.randint(0, 982)
    huellasDeConsulta = random.randint(0, 44)
    edadEmpresarios = random.randint(22, 74)
    noDeAccionistas = random.randint(1, 69)
    noEmpleados = random.randint(1, 500)
    mujeresEnCargosDirectivos = random.randint(0, 25)


    # variables alfanuméricas.
    # ------------------------------------------------
    state = ran(['PAID', 'LATE'])
    usoDeLosRecursos = ran(['CR', 'KT - CO', 'KT - EX', 'SP'])
    plazo = ran(['Menos de 12 meses', '13 a 24 meses', '25 a 36 meses', 'Más de 37 meses'])
    sector = ran(['Comercio', 'Industria', 'Servicios'])
    ingresos = ran(['Growth', 'Scale Up', 'Seed', 'Venture'])
    ubicacion = ran(['Armenia', 'Barranquilla', 'Bello', 'Bogotá D.C.', 'Bucaramanga', 'Cali', 'Cartagena de indias', 'Copacabana', 
                    'Envigado', 'Itagüí', 'La Ceja', 'La Estrella', 'Manizales', 'Marinilla', 'Medellín', 'Neiva', 'Pereira', 
                    'Rionegro', 'Sabaneta', 'Santa Marta'])
    procesosJudiciales = ran(['Si', 'No'])
    alertas = ran(['Si', 'No'])
    websiteEmpresa = ran(['Si', 'No'])
    instagramEmpresa = ran(['Si', 'No'])
    linkedInEmpresa = ran(['Si', 'No'])
    activador = ran(['CommunicationMedia', 'CreditProfessionalContact', 'Email', 'Fenalco', 'FriendOrColleague', 'Internet', 
                    'Newspapers', 'Other', 'Referrer', 'RutaN', 'SocialNetworks'])
    impacto = ran(['Si', 'No'])
    accesoPrevioBanca = ran(['Si', 'No'])
    mujeresEmpresarias = ran(['Si', 'No'])


    # Building Keys and Values:
    # ------------------------------------------------
    keys = ["clientId", "loanId", "state", "arrearDays", "montoAcumulado", "usoDeLosRecursos",
            "plazo", "sector", "ingresos", "ubicacion", "procesosJudiciales", "alertas",
            "scoreBureauEmpresa", "huellasDeConsulta", "websiteEmpresa", "instagramEmpresa",
            "linkedInEmpresa", "edadEmpresarios", "activador", "noDeAccionistas", "impacto",
            "accesoPrevioBanca", "noEmpleados", "mujeresEmpresarias", "mujeresEnCargosDirectivos"]

    values = [clientId, loanId, state, arrearDays, montoAcumulado, usoDeLosRecursos,
            plazo, sector, ingresos, ubicacion, procesosJudiciales, alertas,
            scoreBureauEmpresa, huellasDeConsulta, websiteEmpresa, instagramEmpresa,
            linkedInEmpresa, edadEmpresarios, activador, noDeAccionistas, impacto,
            accesoPrevioBanca, noEmpleados, mujeresEmpresarias, mujeresEnCargosDirectivos]

    # ----------------------------------------------------------------------------------------------------

    new_dict = dict(zip(keys, values))
    return(new_dict)

def generate_data():
    # new empty data structures {dict} & [list]:
    new_dict = {}
    new_list = [] 

    # asking user how many data sets will be generated:
    variable = input('¿Cuántos clientes desea evaluar? ')

    # structure builder: object's array:
    for i in range(0, int(variable)):
        new_list.append({'user{}'.format(i): randomizer()})

    # main object structure:
    new_dict = {'users': new_list}

    # printing required output:
    #print(new_dict)
    new_dict = json.dumps(new_dict)
    #dict_final = json.loads(new_dict)
    
    return new_dict