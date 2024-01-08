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

from drf_extra_fields.fields import Base64ImageField

class OrganizationSerialzer(serializers.ModelSerializer):
    image_url =  Base64ImageField(required=False)
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


class OrganizationFileSerialzer(serializers.Serializer):
    id = serializers.CharField()
    image_url =  Base64ImageField(required=True)

    
    # image_url =  Base64ImageField(required=False)
    # class Meta:
    #     model = Organization
    #     fields = ("id","image_url")

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
        fields = ('id','name','org_type','order_status','note','expected_date',"order_stage"
                  ,'organizationemployee_set' ,'organizationservice_set','geolocation_set','image_url')
        depth = 1

class SimpleOrganizationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id','name',)

from django.core.files import File
import base64

class OrganizationImageSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField(required = False)
    image_url = serializers.CharField(required = False)
    class Meta:
        model = Organization
        fields = ('base64_image', 'id', 'image_url')

    def get_base64_image(self, obj):
        f = open(obj.image_url.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
    
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
    # organizationvisit_set = DeepVisitSerializer(many = True)
    organizationvisit_set = serializers.SerializerMethodField(source='get_organizationvisit_set')
    class Meta:
        model = Organization
        fields = ('id','name','org_type','order_status','note','expected_date',"order_stage"
                  ,'organizationvisit_set','geolocation_set')
        depth = 1
    def get_organizationvisit_set(self, obj):
        return DeepVisitSerializer(obj.organizationvisit_set.filter(is_reviewed = 0),many =True).data
        # return DeepVisitSerializer(obj.organizationvisit_set.all(),many =True).data

# class OrganizationTypeSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = OrganizationType
#         fields = "__all__"

# class OrderStatusSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderStatus
#         fields = "__all__"


# class EmployeeRoleSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeRole
#         fields = "__all__"


# class ServiceTypeSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceType
#         fields = "__all__"


# class ServiceSectionSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceSection
#         fields = "__all__"

