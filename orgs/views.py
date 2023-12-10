from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .models import *



@api_view(['POST'])
def create_organization(request):
    print("create organizations")
    serializer = OrganizationSerialzer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print("create organizations")
        return Response({'status':'succeed', 'message': 'organization_created_successfully'})
    else:
        
        print(serializer.errors)
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


@api_view(['GET']) 
def get_organizations_all(request):
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

