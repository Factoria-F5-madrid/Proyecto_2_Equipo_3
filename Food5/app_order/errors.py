from Food5.app_Bread.models import Bread
from app_drink.errors import error_response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def error_response(status_code, error, message):
    return Response(
        {"status": status_code, "error": error, "message": message},
        status=status_code
    )

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_pan(request, pk):
    pan = get_object_or_404(Bread, pk=pk)
    if request.method == 'GET':
        serializer = BreadSerializer(pan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BreadSerializer(pan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return error_response(400, "Bad Request", serializer.errors)
    elif request.method == 'DELETE':
        pan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@app.route('/bread')
def get_item(id):
    item = busca_en_db(id)
    if not item:
        return error_response(404, "Not Found", "El recurso solicitado no existe")
    return jsonify(item)

@app.errorhandler(404)
def not_found(error):
    return error_response(404, "Not Found", "El recurso solicitado no existe")

# return error_response(400, "Bad Request", "Datos inválidos")

# return error_response(500, "Internal Server Error", "Error inesperado del servidor")