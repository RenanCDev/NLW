from src.views.http_types.http_response import HttpResponse as hrp

def handle_errors(error: Exception) -> hrp:
    return hrp(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
