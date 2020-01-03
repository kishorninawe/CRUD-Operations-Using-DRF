from rest_framework.generics import (ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView)

from app.models import EmployeeModel
from app.serializers import EmployeeSerializer


class EmployeeList(ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreate(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieve(RetrieveAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdate(RetrieveUpdateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDelete(RetrieveDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetails(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
