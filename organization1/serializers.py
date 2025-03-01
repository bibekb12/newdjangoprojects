from .models import Employee, Department
from rest_framework import serializers


class EmployeeListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "emp_fname",
            "emp_lname",
            "emp_fullname",
            "emp_joined",
            "emp_code",
            "emp_department",
        ]

    def to_representation(self, instance):
        return {"instance": instance, "-message": " employee created successfully"}


class EmployeeUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "emp_fname",
            "emp_lname",
            "emp_fullname",
            "emp_joined",
            "emp_code",
            "emp_department",
        ]

    def to_representation(self, instance):
        return {"instance": instance, "-message": " employee updated successfully"}


class EmployeeDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def delete(self, emp_code):
        instance = Employee.objects.get(emp_code=emp_code)
        instance.delete()
        return instance

    def to_representation(self, instance):
        return {"instance": instance, "-message": " employee deleted successfully"}


class DepartmentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DepartmentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def create(self, validated_data):
        validated_data["dep_name"] = validated_data.get("dep_name")
        validated_data["dep_code"] = validated_data.get("dep_code")
        validated_data["dep_isactive"] = validated_data.get("dep_isactive", "Y")
        return super().create(validated_data=validated_data)

    def to_representation(self, instance):
        return {"instance": instance, "-message": " department created successfully"}


class DepartmentUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ["dep_name", "dep_code", "dep_isactive"]

    def delete(self, pk):
        instance = Department.objects.get(pk=pk)
        instance.dep_isactive = "N"
        instance.save()
        return instance

    def to_representation(self, instance):
        return {"instance": instance, "-message": "department updated successfully"}
