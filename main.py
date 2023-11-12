import csv
import json


def load_json_elements(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        groups = json.load(file)
    return groups


def load_csv_elements(csv_file):
    element = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_txt = csv.reader(file)
        for row in csv_txt:
            element.append(row)
            csv_row = ",".join(row)
            print(csv_row)
    return element


def list_dict_fill():
    element = [{}]

    for i in range(len(elements_csv) - 1):
        dic_add = {}
        for j in range(28):
            dic_add[elements_csv[0][j]] = elements_csv[i + 1][j]
        element.append(dic_add)
    return element


groups = load_json_elements('groups.json')
elements_csv = load_csv_elements('elements.csv')
elements = list_dict_fill()


def vyber():
    print("1: Vyhledavani prvku")
    print("2: Periodicka tabulka")
    print("3: Vypocet")
    print("4: Vypnout program")


while True:
    vyber()
    volba = input("Zadej svou volbu: ")
    if volba == "1":
        print("neni dodelano")
    elif volba == "2":
        print("neni dodelano")
    elif volba == "3":
        print("neni dodelano")
    elif volba == "4":
        break
