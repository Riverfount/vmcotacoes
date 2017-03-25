#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import json
import time
from htmltag import a


def cotar():

    moeda = dict()
    try:
        req = requests.get("http://api.promasters.net.br/cotacao/v1/valores")
        moeda = json.loads(req.text)
        for key in moeda["valores"]:
            moeda["valores"][key]["ultima_consulta"] = time.strftime("%Hh.%Mmin. de %d/%b/%Y",
                                                       time.localtime(moeda["valores"][key]["ultima_consulta"]))

            moeda["valores"][key]["valor"] = "%.2f" % moeda["valores"][key]["valor"]

            extraido = str.split(moeda["valores"][key]["fonte"], "-")
            moeda["valores"][key]["fonte"] = extraido[0] + " - " + a(extraido[1].lstrip(), href = extraido[1].lstrip())

        return moeda
    except:
        return moeda

