from organization1.models import Department, Employee
from .serializers import (
    EmployeeCreateSerializers,
    EmployeeListSerializers,
    EmployeeDeleteSerializers,
    EmployeeUpdateSerializers,
    DepartmentListSerializers,
    DepartmentCreateSerlializers,
    DepartmentUpdateSerializers,
)
from rest_framework import permissions
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            serializer_class = EmployeeListSerializers
        elif self.request.method == "POST":
            serializer_class = EmployeeCreateSerializers
        elif self.request.method == "PATCH":
            serializer_class = EmployeeUpdateSerializers
        elif self.request.method == "DELETE":
            serializer_class = EmployeeDeleteSerializers
        return serializer_class


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            serializer_class = DepartmentListSerializers
        elif self.request.method == "POST":
            serializer_class = DepartmentCreateSerlializers
        elif self.request.method == "UPDATE":
            serializer_class = DepartmentUpdateSerializers
        return serializer_class
