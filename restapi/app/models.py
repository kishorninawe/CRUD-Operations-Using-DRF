from django.db import models


class EmployeeModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
