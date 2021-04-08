from flask import Flask
from flask import request
import pyodbc
import json

# import requests

app = Flask(__name__)
app.debug = True

def get_db():
    server = 'tcp:dissoserver.database.windows.net'
    database = 'dissoDB'
    username = 'shirin'
    password = 'Qwerty123'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM myTable")
    row = cursor.fetchone()
    while row:
        return row[0]
        # print(row[0])
        # row = cursor.fetchone()

    # x = requests.get('https://40435.wayscript.io/main')

    return "death"


def get_db_value(params):
    server = 'tcp:dissoserver.database.windows.net'
    database = 'dissoDB'
    username = 'shirin'
    password = 'Qwerty123'

    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    if not params:
        return []

    query = ""
    for k, val in params.items():
        if query:
            query += " AND "
        query += k + "='" + val + "'"

    # print(query)
    cursor.execute("SELECT * FROM myTable WHERE " + query)
    row = cursor.fetchone()
    # print(row)
    ret = []
    while row:
        restaurant = {
            'food': row[0],
            'pricerange': row[1],
            'phone': row[2],
            'area': row[3],
            'addr': row[4],
            'postcode': row[5],
            'name': row[6]
        }
        ret.append(restaurant)
        row = cursor.fetchone()

    return ret


def params_dict(tracker):
    search_params = dict()

    params = ["area", "name", "pricerange", "food"]

    for param in params:
        try:
            slot = tracker[param]
            if slot != None:
                search_params[param] = slot[0]
        except:
            pass

    return search_params


# def get_corresponding_value(params):

#     res = []

#     main_db = get_db()

#     for k, val in main_db.items():
#         full_match = True

#         for p_k, p_val in params.items():

#             if not val[p_k] == p_val:
#                 full_match = False

#         if full_match:
#             res.append(val)
#     # print(res)
#     return res

def action_suggest(tracker):
    print("Tracker:")
    print(tracker)
    search_params = params_dict((tracker['queryResult'])['parameters'])
    full_results = get_db_value(search_params)

    response = {
          "fulfillmentMessages": [
            {
              "text": {
                "text": ["No restaurants with those details were found"]
              }
            }

          ],
          "outputContexts": [
            {
              "name": ((tracker['queryResult'])['outputContexts'])[0]['name'],
              "lifespanCount": 10,
              "parameters": {}
            }
          ]
        }

    # print(full_results)
    if bool(full_results):
        for r in full_results:
            tex=str("name: " +r['name'] + ", phone: " + r['phone'] + ", address: " + r['addr'])
            # print(tex)
            ((response['fulfillmentMessages'])[0]['text'])['text'][0] = tex
            (response['outputContexts'])[0]['parameters'] = {'slot': r['name']}
            break

    return json.dumps(response)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/get_recc', methods=['POST'])
def api_gh_message():
    # main_db = get_db()
    # print("hi")
    # return "it's postin"
    return action_suggest(request.json)


@app.route("/christel")
def chris_brains():
    return get_db()


if __name__ == '__main__':
    # main_db = get_db()
    # debug = True
    app.run()
