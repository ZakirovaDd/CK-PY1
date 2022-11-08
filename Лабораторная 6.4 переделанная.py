import json

INPUT_FILE = "input.csv"



def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
    with open(filename, encoding="utf-8") as file:
        list_json = []
        headers = file.readline().strip().split(delimiter)
        for rows in file:
            if rows.split(delimiter) != headers:
                new_rows = rows.strip().split(delimiter)
                list_json += [{headers[i]: new_rows[i] for i in range(0,len(new_rows))}]
        return list_json

# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
