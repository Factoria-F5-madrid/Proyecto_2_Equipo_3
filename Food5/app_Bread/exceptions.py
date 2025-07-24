from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        code = response.status_code
        response.data = {
            "status": code,
            "error": response.status_text,
            "message": response.data.get('detail', 'Ocurrió un error')
        }
    return response
