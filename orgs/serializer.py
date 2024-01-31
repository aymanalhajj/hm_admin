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


class OrganizationImageFileSerialzer(serializers.Serializer):
    id = serializers.CharField()
    image_url =  Base64ImageField(required=True)

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import serializers
from drf_extra_fields.fields import Base64FileField, Base64ImageField
import filetype

## defenition
class MyCustomBase64FileField(Base64FileField):
    """
    A custom serializer field to handle base64-encoded files.
    """
    ALLOWED_MIME_TYPES = {
        'image/jpeg': 'jpg',
        'image/png': 'png',
        'application/pdf': 'pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    }

    ALLOWED_TYPES = ['pdf', 'docx', 'jpg', 'jpeg', 'png']

    def get_file_extension(self, filename, decoded_file):
        extension = filetype.guess_extension(decoded_file)
        return extension

    def to_internal_value(self, data):
        if isinstance(data, str):
            return super().to_internal_value(data)
        return data

## Usge
class OrganizationFileSerialzer(serializers.ModelSerializer):
    file = MyCustomBase64FileField(required=True)
    class Meta:
        model = OrganizationFile
        fields = ("organization","file","description")
    # def create(self,obj):
    #     print(obj.get('organization'))
    #     OrganizationFile.objects.create(organization_id = obj.get('organization'),description = obj.get('description'))
    


class VisitReviewSerializer(serializers.Serializer):
    visit_id = serializers.IntegerField()
    review_note = serializers.CharField()


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationVisit
        fields = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','organization','visitor',)

class VisitTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTask
        fields = ('organization','note')

class VisitTaskNoteSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    note = serializers.CharField(required=False,allow_blank=True)

class ComplexOrganizationSerialzer(serializers.ModelSerializer):
    # organizationemployee_set = ComplexOrganizationEmployeeSerialzer(many = True)
    # organizationservice_set = ComplexOrganizationServiceSerialzer(many = True)
    class Meta:
        model = Organization
        fields = ('id','name','org_type','order_status','note','expected_date',"order_stage"
                  ,'organizationemployee_set' ,'organizationservice_set','geolocation_set','image_url','organizationfile_set')
        depth = 1

class SimpleOrganizationSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id','name',)

class SimpleVisitTaskSerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField(source='get_organization_name')
    organization_id = serializers.SerializerMethodField(source='get_organization_id')
    task_id = serializers.SerializerMethodField(source='get_task_id')
    class Meta:
        model = VisitTask
        fields = ('task_id','organization_id','organization_name')
        depth = 1
    def get_organization_name(self, obj):
        return obj.organization.name
    def get_organization_id(self, obj):
        return obj.organization.id
    def get_task_id(self, obj):
        return obj.id
 
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

class DeepVisitSerializer(serializers.ModelSerializer):
    visitor = VisitorSerializer(many = False)
    class Meta:
        model = OrganizationVisit
        fields = ('id','is_reviewed','service_type','service_section','visit_state','visit_note','visitor',)
        depth = 1
