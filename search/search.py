import json
from translate import Translator
from typing import Any

def search_id(name: str) -> Any:
    with open('current.city.list.txt', encoding='utf8') as f:
        json_city = json.load(f)

    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(name)
    for i in json_city:
        if i['name'] == translation:
            id_city = int(i['id'])
            break
        else:
            id_city = False

    return id_city
