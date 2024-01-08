from rest_framework import serializers
from .models import *
from geo_location.serializer import GeoLocationSerializer

class OrganizationTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationType
        fields = "__all__"

class OrderStatusSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class EmployeeRoleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = "__all__"


class ServiceTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"


class ServiceSectionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = "__all__"


class OrderStageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderStage
        fields = "__all__"


class VisitStatusSerialzer(serializers.ModelSerializer):
    class Meta:
        model = VisitStatus
        fields = "__all__"

