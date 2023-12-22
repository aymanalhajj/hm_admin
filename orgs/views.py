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
        
        return Response({'status':'succeed', 'message':'organization_created_successfully'})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})


@api_view(['POST'])
def visit_organization(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = VisitSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        visit_instance = serializer.save()
        visit_instance.visitor = auth_status['user']
        visit_instance.save()
        OrganizationService.objects.filter(
            service_section_id = visit_instance.service_section_id,
            service_type_id = visit_instance.service_type_id,
            organization_id = visit_instance.organization_id).update(
                is_visited = 1
            )
        return Response({'status':'succeed', 'message':'visit_created_successfully',"data":VisitSerializer(visit_instance).data})
    else:
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def review_organization_visit(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    serializer = VisitReviewSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        OrganizationVisit.objects.filter(id = data.get("visit_id")).update(
            review_note = data.get("review_note"),
            reviewer = auth_status['user_id'],
            is_reviewed = 1
            )
        return Response({'status':'succeed', 'message':'visit_reviewed_successfully'})
    else:
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

from django.db.models import Subquery, OuterRef,Q
from django.db.models.expressions import RawSQL
import operator
import functools
# query = functools.reduce(
#     operator.or_, 
#     (Q(firstname=fn, lastname=ln) for fn, ln in zip(first_list, last_list))
#     )

@api_view(['GET']) 
def get_organizations_for_visit(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    manager_user = ServiceSection.objects.filter(section_manager = auth_status['user_id'])
    if manager_user.count()>0:
        objects = Organization.objects.filter( id__in = Subquery(OrganizationService.objects.filter(is_visited = 0, service_section__in = Subquery(manager_user.values('id'))).values('organization')))
        serializer = ComplexOrganizationSerialzer(objects, many = True)
        services = OrganizationService.objects.filter(is_visited = 0,service_section__in = Subquery(manager_user.values('id')))
        service_serializer =  OrganizationServiceSerialzer(services,many = True)
        return Response({"orgs":serializer.data,"authorized_services" : service_serializer.data })
    section_employees = ServiceSectionEmployee.objects.filter(employee = auth_status['user_id'])
    if section_employees.count()>0:
        objects = Organization.objects.filter(id__in = RawSQL("select organization_id from orgs_OrganizationService where is_visited = 0 and ( service_section_id, service_type_id) in %s ",[list(section_employees.values_list("service_section","service_type"))])) 
        serializer = ComplexOrganizationSerialzer(objects, many = True)
        services = OrganizationService.objects.raw("select * from orgs_OrganizationService where is_visited = 0 and ( service_section_id, service_type_id) in %s ",[list(section_employees.values_list("service_section","service_type"))])
        service_serializer =  OrganizationServiceSerialzer(services,many = True)
        return Response({"orgs":serializer.data,"authorized_services" : service_serializer.data })
    return Response([])

@api_view(['GET']) 
def get_organizations_for_review(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    manager_user = ServiceSection.objects.filter(section_manager = auth_status['user_id'])
    if manager_user.count()>0:
        objects = Organization.objects.filter(id__in = Subquery(OrganizationVisit.objects.filter(is_reviewed =  0, service_section__in = Subquery(manager_user.values('id'))).values('organization')))
        serializer = OrganizationForReviewSerialzer(objects, many = True)
        # services = OrganizationService.objects.filter(service_section__in = Subquery(manager_user.values('id')))
        # service_serializer =  OrganizationServiceSerialzer(services,many = True)
        return Response(serializer.data)
    return Response([])
    


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

