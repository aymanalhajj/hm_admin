from rest_framework import serializers
from .models import *
from geo_location.serializer import GeoLocationSerializer

class OrganizationEmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationEmployee
        fields = ('id','name','mobile','organization','role')
        # depth = 1

class ComplexOrganizationEmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationEmployee
        fields = ('id','name','mobile','organization','role')
        depth = 1


class ComplexOrganizationServiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationService
        fields = "__all__"
        depth = 1

class OrganizationServiceSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationService
        fields = "__all__"

class OrganizationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

class OrganizationWithLocationSerialzer(serializers.Serializer):
    organization = OrganizationSerialzer(source = "*")
    geo_location = GeoLocationSerializer(source = "*")
    class Meta:
        # model = Organization
        fields = ('organization','geo_location')

class ComplexOrganizationSerialzer(serializers.ModelSerializer):
    # organizationemployee_set = ComplexOrganizationEmployeeSerialzer(many = True)
    # organizationservice_set = ComplexOrganizationServiceSerialzer(many = True)
    class Meta:
        model = Organization
        fields = ('id','name','org_type','order_status','note','expected_date','organizationemployee_set','organizationservice_set')
        depth = 1

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

