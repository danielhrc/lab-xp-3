import math
import csv
import time
import requests

from main import run_query


loc = []
headers = ['name','owner','url','stargazers','issues','primaryLanguage']

with open('resul_tado.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, fieldnames=['name', 'owner'], delimiter=';', quotechar='|')
    for row in spamreader:
        if row['name'] == 'name':
            continue
        try:
            print(row['name'], row['owner'])
            run_query(row['name'], row['owner'])

        except:
            continue

csvfile.close()

