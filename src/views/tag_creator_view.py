from src.views.http_types.http_request import HttpRequest as hrq
from src.views.http_types.http_response import HttpResponse as hrp

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: hrq):
        body = http_request.body
        product_code = body["product_code"]

        print('Im in my view!')

        return hrp(status_code=200, body={"hello": "world"})
