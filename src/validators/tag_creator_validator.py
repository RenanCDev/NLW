from cerberus import Validator as vl
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError as uee

'''
{
    "product_code": "123"
}
'''

def tag_creator_validator(request: any) -> None:
    body_validator = vl({
        "product_code": { "type": "string", "required": True, "empty": False }
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise uee(body_validator.errors)