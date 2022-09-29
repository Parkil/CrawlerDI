import json


def __default(obj):
    if hasattr(obj, 'json_dict'):
        return obj.json_dict()
    else:
        json_encoder: json.JSONEncoder = json.JSONEncoder()
        return json_encoder.default(obj)


def json_dump(param_obj: object) -> str:
    return json.dumps(param_obj, ensure_ascii=False, default=__default)
