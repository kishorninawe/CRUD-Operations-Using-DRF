from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import EmployeeModel
from app.serializers import EmployeeSerializer
from rest_framework import status


class EmployeeList(APIView):
    def get(self, request):
        employees = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetails(APIView):
    def get(self, request, pk):
        employee = EmployeeModel.objects.filter(id=pk)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            employee = EmployeeModel.objects.get(id=pk)
        except EmployeeModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = EmployeeModel.objects.filter(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
