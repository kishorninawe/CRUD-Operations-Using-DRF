from rest_framework.viewsets import ModelViewSet

from app.models import EmployeeModel
from app.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
