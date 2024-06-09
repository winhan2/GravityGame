# coding: utf-8
import json

def dic(*args, **kwargs) -> dict:
    def read_lang_json(route):
        with open(route, mode='rt', encoding='utf-8') as rljf:
            lj = rljf.read()
        return lj

    rljr = read_lang_json(*args, **kwargs)
    ld = json.loads(rljr)

    return ld


if __name__ == '__main__':
    LANG_DIC = dic(r"..\conf\lang\zh-cn\main_cmd.json")
    print(LANG_DIC)