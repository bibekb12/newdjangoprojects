from .models import Employee, Department
from rest_framework import serializers


class EmployeeListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        field = "__all__"


class EmployeeCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        return {instance, " employee created successfully"}


class EmployeeUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        return {instance, " employee updated successfylly"}


class EmployeeDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "emp_name", "emp_status"]

    def to_representation(self, instance):
        return {instance, " employee deleted successfully"}


class DepartmentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DepartmentCreateSerlializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def to_representation(self, instance):
        return {instance, " department created successfully"}


class DepartmentUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["id", "dep_name", "dep_status"]

    def to_representation(self, instance):
        return {instance, " department updated successfully"}
