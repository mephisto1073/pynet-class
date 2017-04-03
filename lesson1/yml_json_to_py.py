#!/usr/bin/env python

import pprint
import yaml
import json

with open('py_2_yml.yml') as f:
    lista_a = yaml.load(f)
pprint.pprint(lista_a)

with open('py_2_json.json') as g:
    lista_b = json.load(g) 
pprint.pprint(lista_b)
