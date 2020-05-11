import csv
import os
import time
import requests
from query import query
from query_issue import query_issue


def run_query(repo, owner):
    names = []
    to_csv = []

    after = ''

    dado = ''
    cursor = ''
    have_next_page = True
    page = 0
    headers = {"Authorization": "token 072ffc3dd4deb67c214a2236deab30482c262b45"}
    print(repo, owner)
    query_aux = query_issue % (repo, owner, '%s')

    mquery = query_aux % after
    nodes = list()
    f = open("page.txt", "a")
    have_next_page = True
    while have_next_page:

        request = requests.post('https://api.github.com/graphql', json={'query': mquery}, headers=headers)
        print('page:' + str(page))
        print(request.status_code)
        if request.status_code == 200:
            result = request.json()
            nodes += result['data']['repository']['issues']['nodes']
            have_next_page = result["data"]['repository']["issues"]["pageInfo"]["hasNextPage"]

            if have_next_page:
                f.write(result["data"]['repository']["issues"]["pageInfo"]["endCursor"])

            page += 1

            after = ', after:"' + result["data"]['repository']["issues"]["pageInfo"]["endCursor"] + '"'
            mquery = query_aux % after

    f.close()
    for d in nodes:
        row = {}
        for keys in d.keys():
            if keys not in names:
                names.append(keys)
            row.update({keys: d[keys]})
        to_csv.append(row)

    try:
        # Create target Directory
        os.mkdir(repo)
        print("Directory ", repo, " Created ")
    except FileExistsError:
        print("Directory ", repo, " already exists")

    with open(repo + '/' + repo + '.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=names, delimiter=';')
        writer.writeheader()
        for i in to_csv:
            writer.writerow(i)
