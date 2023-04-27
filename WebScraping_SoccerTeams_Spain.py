#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:50:46 2023

@author: ropger
"""

import requests


from bs4 import BeautifulSoup
import pandas as pd
                          
url = 'https://mexico.as.com/resultados/futbol/primera/clasificacion/'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')



eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()

count = 0
for nombre in eq:
    if count < 20:
        equipos.append(nombre.text)
    else:
        break
    count +=1
print(equipos)



pt = soup.find_all('td', class_='destacado')

puntos = list()

count = 0
for nombre in pt:
    if count < 20:
        puntos.append(nombre.text)
    else:
        break
    count +=1
print(puntos)




df = pd.DataFrame({'Nombre':equipos, 'Puntos':puntos}, index=list(range(1,21)))
               
df.to_csv('PuntajeEquiposX.csv', index=False)             