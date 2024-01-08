from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *

import logging
# Create a logger for this file
logger = logging.getLogger(__file__)
# logger.debug("This logs a debug message.")


@api_view(['GET']) 
def get_org_types(request):
    logger.info("get_org_types")
    # raise Exception("This is a handled exception")
    objects = OrganizationType.objects.all()
    serializer = OrganizationTypeSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_order_status(request):
    objects = OrderStatus.objects.all()
    serializer = OrderStatusSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_visit_status(request):
    objects = VisitStatus.objects.all()
    serializer = VisitStatusSerialzer(objects, many = True)
    return Response(serializer.data)


@api_view(['GET']) 
def get_order_stages(request):
    objects = OrderStage.objects.all()
    serializer = OrderStageSerialzer(objects, many = True)
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

