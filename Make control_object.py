import json


def get_control_object():
    c_o = []

    with open('response.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for i in data['items']:
            c_o.append(i['id'])
    print(len(c_o), c_o)


def get_id_80020():
    id_80020 = []

    with open('response.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for i in data['items']:
            id_80020.append(i['xmlFileId'])
    print(len(id_80020), id_80020)

get_id_80020()


