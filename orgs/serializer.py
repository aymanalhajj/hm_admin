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

class EngineerNoteSerialzer(serializers.Serializer):
    organization = serializers.CharField()
    engineer_note = serializers.CharField()

class VisitReviewSerializer(serializers.Serializer):
    visit_id = serializers.IntegerField()
    review_note = serializers.CharField()


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationVisit
        fields = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','organization','visitor',)

class ComplexOrganizationSerialzer(serializers.ModelSerializer):
    # organizationemployee_set = ComplexOrganizationEmployeeSerialzer(many = True)
    # organizationservice_set = ComplexOrganizationServiceSerialzer(many = True)
    class Meta:
        model = Organization
        fields = ('id','name','org_type','order_status','note','expected_date',"admin_note","engineer_note","order_stage"
                  ,'organizationemployee_set' ,'organizationservice_set','geolocation_set')
        depth = 1

class VisitorSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()

# class VisitorSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = UserAccount
    #     fields = ('first_name','last_name','username')

class DeepVisitSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer(many = False)
    class Meta:
        model = OrganizationVisit
        fields = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','visitor',)
        depth = 1

class OrganizationForReviewSerialzer(serializers.ModelSerializer):
    # organizationemployee_set = ComplexOrganizationEmployeeSerialzer(many = True)
    organizationvisit_set = DeepVisitSerializer(many = True)
    class Meta:
        model = Organization
        fields = ('id','name','org_type','order_status','note','expected_date',"admin_note","engineer_note","order_stage"
                  ,'organizationvisit_set','geolocation_set')
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

