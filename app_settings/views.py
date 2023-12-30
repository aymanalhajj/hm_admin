from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from orgs.serializer import *

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

