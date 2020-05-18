import json

import requests
from query_stack import query
to_json = []


tags = ['JavaScript', 'vue', 'C++', 'Shell', 'Java', 'TypeScript', 'Python', 'Jupyter Notebook', 'CSS', 'Go','dart']

has_next = True
page = 1
for tag in tags:
    while has_next:
        request = requests.get(query % (page, tag))
        to_json.append({'items' : request.json()['items']})
        if not request.json()['has_more']:
            has_next = False
        else:
            page += 1
    with open('stack/' + tag + '.txt', 'w') as outfile:
        json.dump(to_json, outfile)
    outfile.close()
