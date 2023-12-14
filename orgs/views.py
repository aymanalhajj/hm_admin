from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from geo_location.models import GeoLocation
from .models import *



@api_view(['POST'])
def create_organization(request):
    serializer = OrganizationSerialzer(data = request.data)
    if serializer.is_valid():
        org = serializer.save()
        print("create organizations")
        return Response({'status':'succeed', 'message': 'organization_created_successfully',"data":org.id})
    else:
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def create_organization_with_location(request):
    serializer = OrganizationWithLocationSerialzer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        organization = Organization.objects.create(name = data.get("name"),
                                                   org_type= data.get("org_type"),
                                                   order_status=data.get("order_status"),
                                                   note=data.get("note"),
                                                   expected_date=data.get("expected_date"))
        
        geo_location = GeoLocation.objects.create(longitude = data.get("longitude"),
                                                  latitude= data.get("latitude"),
                                                  country_name=data.get("country_name"),
                                                  locality=data.get("locality"),
                                                  address=data.get("address"),
                                                  organization=organization)
        return Response({'status':'succeed', 'message':'organization_created_successfully',"data": organization.id})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})


@api_view(['POST'])
def update_organization_by_engineer(request):
    serializer = EngineerNoteSerialzer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data.get("engineer_note"))
        Organization.objects.filter(id = data.get("organization")).update(engineer_note = data.get("engineer_note"))
        # organization.engineer_note = data.get("engineer_note")
        # organization.save()
        
        return Response({'status':'succeed', 'message':'organization_created_successfully'})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})


@api_view(['POST'])
def create_organization_emp(request):
    serializer = OrganizationEmployeeSerialzer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'succeed', 'message': 'organization_emp_created_successfully'})
    else:
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def create_organization_service(request):
    serializer = OrganizationServiceSerialzer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print('good')
        return Response({'status':'succeed', 'message': 'organization_service_created_successfully'})
    else:
        print(serializer.errors)
        return Response({'status':'failed','errors': serializer.errors})

from custom_auth.models import JWTAuthentication

@api_view(['GET']) 
def get_organizations_all(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    objects = Organization.objects.all()
    serializer = ComplexOrganizationSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_org_emps_all(request):
    objects = OrganizationEmployee.objects.filter(organization= request.GET.get("org_id")).all()
    serializer = OrganizationEmployeeSerialzer(objects, many = True)
    return Response(serializer.data)

@api_view(['GET']) 
def get_org_service_all(request):
    objects = OrganizationService.objects.filter(organization= request.GET.get("org_id")).all()
    serializer = OrganizationServiceSerialzer(objects, many = True)
    return Response(serializer.data)

@api_view(['GET']) 
def get_org_types(request):
    objects = OrganizationType.objects.all()
    serializer = OrganizationTypeSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_order_status(request):
    objects = OrderStatus.objects.all()
    serializer = OrderStatusSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_emp_roles(request):
    objects = EmployeeRole.objects.all()
    serializer = EmployeeRoleSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_service_types(request):
    objects = ServiceType.objects.all()
    serializer = ServiceTypeSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_service_sections(request):
    objects = ServiceSection.objects.all()
    serializer = ServiceSectionSerialzer(objects, many = True)
    return Response(serializer.data)

