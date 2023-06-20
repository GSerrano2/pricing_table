import os
import json
import fnmatch
from variables import env

def getData():
    estimate = getFisrtJsonFromDir(env.ESTIMATE)

    with open(env.ESTIMATE + "/" + estimate, 'r') as estimate:
        data = json.load(estimate)
        services = data['Grupos']['Servicios']

        servicesList = getAttribute(services, ['Nombre del servicio'])
        servicesDescription = getAttribute(services, ['Descripción'])

        servicesInitialCosts = getAttribute(services, ['Costo del servicio', 'inicial'])
        servicesMontlhyCosts = getAttribute(services, ['Costo del servicio', 'mensual'])
        servicesAnualCosts = getAttribute(services, ['Costo del servicio', '12 meses'])
        
        CurrencyType = data['Metadatos']['Divisa']
        servicesCurrencyType = []
        servicesQuantity = []
        for _ in services:
            servicesCurrencyType.append(CurrencyType)
            servicesQuantity.append("-")

        servicesObservations = getAttribute(services, ['Propiedades'])

        data = []
        data.append(servicesList)
        data.append(servicesDescription)
        #data.append(servicesInitialCosts)
        data.append(servicesMontlhyCosts)
        data.append(servicesAnualCosts)
        data.append(servicesCurrencyType)
        data.append(servicesQuantity)
        data.append(servicesObservations)
    return data

def getFisrtJsonFromDir(dir):
     for file in os.listdir(dir):
        if fnmatch.fnmatch(file, '*.json'):
            return file
        
def getAttribute(services, attributes=[]):
    list = []
    for s in services:
        a = getAttributeData(s, attributes.copy())
        list.append(a)
    return list

def getAttributeData(service, attributes):
    if (len(attributes) == 1):
            return service[attributes[0]]
    for _ in attributes:
        first = attributes.pop(0)
        data = getAttributeData(service[first], attributes)
    return data
