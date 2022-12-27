# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from lxml import html

encabezados ={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    #cadena que contiene los valores de los encabezados que estoy utilizando para evitar ser confundido como un bot y baneado
}

url = "https://www.wikipedia.org/"
respuesta = requests.get(url,headers = encabezados) #funcion que hace los requerimientos y recive como parametro  la url
#asi  obtengo el arbol html

"user-agent" # variable que define a quien hace el requerimiento
#viene en los encabezados del request

#print(respuesta.text) aqui viene el codigo html
parser = html.fromstring(respuesta.text) #convierte el codigo en texto del que se puede extraer informacion

ingles = parser.get_element_by_id("js-link-box-en") #me devuelve una clase con lo requerido
print(ingles.text_content())

ingles2=parser.xpath("//a[@id = 'js-link-box-en']/strong/text()") #haciendo con xpath
print(ingles2)

idiomas=parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()") #haciendo con xpath
print(idiomas)

idiomas2=parser.find_class('central-featured-lang') #haciendo con lxml
for lengua in idiomas2:
    print(lengua.text_content())