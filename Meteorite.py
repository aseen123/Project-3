import json

file = 'Meteorite_Landings_Assignment.csv'

with open('Meteorite_Landings_Assignment.csv', 'r',encoding ='utf-8') as file:
    lines = [line.rstrip() for line in file]

results = []

for line in lines[1:]:
            words = line.split(',')
            results.append((words[0], words[1:]))

print('\n .csv file output \n') 

print(results[:5])

print()

dictionary = {}

headers = lines[0].split(',')

def convert_to_number(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

with open('Meteorite_Landings_Assignment.csv', 'r', encoding='utf-8') as file:
    for line in file.readlines()[1:]:
        words = line.strip().split(',')

        row_dict = {headers[i]: convert_to_number(words[i]) for i in range(len(headers))}

        key = words[0]
        
        dictionary[key] = row_dict

    print('\n dictionary output \n')

    print(list(dictionary.values())[:5])

    values_list = list(dictionary.values())

    print('\n dictionary into list \n')
    print(values_list[:5])

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(values_list, json_file, ensure_ascii=False, indent=4)

with open('output.json', 'r', encoding='utf-8') as json_file:
    output = json.load(json_file)

    print('\n Converted json file output \n')
    print(json.dumps(output[:5], indent=4))






   
     






