from src.views.http_types.http_response import HttpResponse as hrp
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError as uee

def handle_errors(error: Exception) -> hrp:
    if isinstance(error, uee):
        return hrp(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )


    return hrp(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
