from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import EmployeeModel
from app.serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employee = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):
    if request.method == 'GET':
        employee = EmployeeModel.objects.filter(id=pk)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        try:
            employee = EmployeeModel.objects.get(id=pk)
        except EmployeeModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee = EmployeeModel.objects.filter(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
