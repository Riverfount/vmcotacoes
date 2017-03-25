#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import json
import time
import re


def cotar():
    moeda = dict()
    try:
        req = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
        moeda = json.loads(req.text)
        for key in moeda["valores"]:
            moeda["valores"][key]["ultima_consulta"] = time.strftime("%Hh.%Mmin. de %d/%b/%Y",
                                                                     time.localtime(moeda["valores"][key]["ultima_consulta"]))
            moeda["valores"][key]["valor"] = "%.2f" % moeda["valores"][key]["valor"]
        return moeda
    except Exception as err:
        return moeda

'''
if __name__ == "__main__":
    dicionario = cotar()
    print(dicionario)
    if dicionario:
        dicionario["valores"]["EUR"]["valor"] = "%.2f" % dicionario["valores"]["EUR"]["valor"]
        print(dicionario["valores"]["EUR"]["valor"])
'''