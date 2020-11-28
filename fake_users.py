import requests
import csv


NUMBER_OF_USERS = 50


users = []
for r in range(NUMBER_OF_USERS):

    r = requests.get("https://randomuser.me/api/?nat=us")
    r = r.json()["results"][0]

    user = {
        "name": r["name"]["first"] + ' ' +  r["name"]["last"],
        "slackname": '@'+r["name"]["first"].lower(),
    }

    users.append(user)

csv_file = 'users.csv'
csv_columns = ["name", "slackname"]

for u in users:
    print(u["name"])

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, lineterminator='\n')
        writer.writeheader()
        writer.writerows(users)
except IOError:
    print("I/O error")
