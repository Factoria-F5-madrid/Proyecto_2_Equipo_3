from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DessertSerializer

@api_view(['GET', 'POST'])
def crear_dessert(request):
    if request.method == 'POST':
        serializer = DessertSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # GET: devolver formulario vacío para navegador
    serializer = DessertSerializer(context={'request': request})
    return Response(serializer.data)

"""
Este archivo no contiene vistas.
Las vistas están distribuidas en las apps individuales del proyecto.
"""