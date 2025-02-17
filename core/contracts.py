USER_DATA_SCHEME = {
    "type" : "object",
    "properties": {
        "id" : {"type": "number"},
        "email" : {"type": "string"},
        "first_name" : {"type": "string"},
        "last_name" : {"type": "string"},
        "avatar" : {"type": "string"},
    },
    "required" : ["id", "email", "first_name", "last_name", "avatar"]
}
LIST_DATA_SCHEME = {
    "type" : "object",
    "properties": {
        "id" : {"type": "number"},
        "name" : {"type": "string"},
        "year" : {"type": "number"},
        "color" : {"type": "string"},
        "pantone_value" : {"type": "string"},
    },
    "required" : ["id", "name", "year", "color", "pantone_value"]
}