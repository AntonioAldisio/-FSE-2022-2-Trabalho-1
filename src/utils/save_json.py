import json

def save_json(dir: str, dictionary: dict):
    try:
        print('dir {}'.format(dir))
        json_object = json.dumps(dictionary, indent=4)
        with open(dir, "w", encoding='utf-8') as outfile:
            outfile.write(json_object)
        print('Arquivo salvo com sucesso')
    except Exception as e:
        print('Erro no save_json {}'.format(e))