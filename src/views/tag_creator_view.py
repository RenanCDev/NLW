from src.views.http_types.http_request import HttpRequest as hrq
from src.views.http_types.http_response import HttpResponse as hrp
from src.controllers.tag_creator_controller import TagCreatorController as tcc

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: hrq):
        tag_creator_controller = tcc()

        body = http_request.body
        product_code = body["product_code"]

        formatted_response = tag_creator_controller.create(product_code)

        return hrp(status_code=200, body=formatted_response)
