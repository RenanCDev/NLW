from cerberus import Validator as vl

body = {
    "data": {
        "elemento1": 123.98,
        "elemento2": "Hello World!",
        "elemento3": "123"
    }
}

body_validator = vl({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": True },
            "elemento3": { "type": "string", "required": False, "empty": False },
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print(response)
