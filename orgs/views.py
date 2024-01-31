from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
import os
from geo_location.models import GeoLocation
from app_settings.models import *
from .models import *
from custom_auth.models import JWTAuthentication
from django.db.models import Subquery, OuterRef,Q
from django.db.models.expressions import RawSQL
import logging
# Create a logger for this file
logger = logging.getLogger(__file__)
# logger.debug("This logs a debug message.")
# logger.info("This logs an info message.")
# logger.warn("This logs a warning message.")
# logger.error("This logs an error message.")
# logger.exception("This logs an exception.")

@api_view(['POST'])
def update_organization_location(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = GeoLocationSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        geo_location, created = GeoLocation.objects.get_or_create(organization_id=data.get("organization"))
        geo_location.longitude = data.get("longitude")
        geo_location.latitude= data.get("latitude")
        geo_location.country_name=data.get("country_name")
        geo_location.locality=data.get("locality")
        geo_location.address=data.get("address")
        geo_location.save()
        return Response({'status':'succeed', 'message':'location_updated_successfully',"data": geo_location.id})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def create_organization_with_location(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = OrganizationWithLocationSerialzer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        organization = Organization.objects.create(name = data.get("name"),
                                                   org_type= data.get("org_type"),
                                                   order_status=data.get("order_status"),
                                                   order_stage_id = 1,
                                                   note=data.get("note"),
                                                   expected_date=data.get("expected_date"),
                                                   employee = auth_status['user'],
                                                   image_url = data.get("image_url"))        
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
def create_organization_emp(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = OrganizationEmployeeSerialzer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'succeed', 'message': 'organization_emp_created_successfully'})
    else:
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def create_organization_service(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = OrganizationServiceSerialzer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print('good')
        return Response({'status':'succeed', 'message': 'organization_service_created_successfully'})
    else:
        print(serializer.errors)
        return Response({'status':'failed','errors': serializer.errors})


@api_view(['POST'])
def upload_organization_image(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    serializer = OrganizationImageFileSerialzer(data = request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        organization = Organization.objects.get(id = data.get("id"))
        if(organization.image_url != None and organization.image_url != ""):
            old_file_path = organization.image_url.path
            #Delete old file when upload new one
            if os.path.exists(old_file_path):
                os.remove(old_file_path)    
        organization.image_url = data.get('image_url')
        organization.save()

        
        return Response({'status':'succeed', 'message':'image_uploaded_successfully'})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def upload_organization_file(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    serializer = OrganizationFileSerialzer(data = request.data)
    if serializer.is_valid():
        org_file = serializer.save()
        org_file.created_by = auth_status['user']
        org_file.save()
        return Response({'status':'succeed', 'message':'file_uploaded_successfully'})
    else:
        print({'status':'failed','errors': serializer.errors})
        return Response({'status':'failed','errors': serializer.errors})

@api_view(['POST'])
def remove_organization_file(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    if ("id" in request.headers):
        file_id = request.headers["id"]
        if OrganizationFile.objects.filter(pk= file_id).exists():
            org_file = OrganizationFile.objects.get(id = file_id)
            if(org_file.file != None and org_file.file != ""):
                old_file_path = org_file.file.path
                #Delete old file when upload new one
                if os.path.exists(old_file_path):
                    os.remove(old_file_path)   
            org_file.delete()
            return Response({'status':'succeed', 'message':'file_removed_successfully'})
        else:
            return Response({'status':'failed', 'message':'file does not exist'})
    else:
        return Response({'status':'failed', 'message':'id must be passed'})

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
def submit_organization_for_study(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    if("id" in request.headers):
        Organization.objects.filter(id = request.headers["id"]).update(order_stage = 2)
        return Response({'status':'succeed', 'message':'organization_submited_successfully'})
    else:
        return Response({'status':'failed','message': 'organization id not passed'})

@api_view(['POST'])
def start_organization_visit_task(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    if("id" in request.headers):
        task = VisitTask.objects.create(organization_id = request.headers["id"], visitor = auth_status['user'],task_state_id =1 )
        return Response({'status':'succeed', 'message':'task_started_successfully'})
    else:
        return Response({'status':'failed','message': 'organization id not passed'})

@api_view(['POST'])
def finish_organization_visit_task(request):
    auth_status = JWTAuthentication.authenticate(request)
    serializer = VisitTaskNoteSerializer(data = request.data)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    if serializer.is_valid():
        task = VisitTask.objects.get(id = serializer.validated_data.get("task_id"), visitor = auth_status['user'])
        
        task.note = serializer.validated_data.get("note")
        task.finished_at = date.today()
        task.task_state_id =  "2"
        task.save()

        Organization.objects.filter(id = task.organization_id).update(order_stage = 1)

        return Response({'status':'succeed', 'message':'task_finished_successfully'})
    else:
        return Response({'status':'failed','errors': serializer.errors})
    
@api_view(['GET']) 
def get_new_visit_tasks(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    objects = Organization.objects.filter(order_stage = 4).exclude(id__in = Subquery(VisitTask.objects.filter(task_state=1, visitor = auth_status['user_id']).values('organization_id')))
    serializer = SimpleOrganizationSerialzer(objects, many = True)
    return Response(serializer.data)

@api_view(['GET']) 
def get_in_progress_visit_tasks(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    # objects = Organization.objects.filter(order_stage = 4).filter(id__in = Subquery(VisitTask.objects.filter(task_state=1, visitor = auth_status['user_id']).values('organization_id')))
    objects = VisitTask.objects.filter(task_state=1, visitor = auth_status['user_id'])
    
    serializer = SimpleVisitTaskSerializer(objects, many = True)
    return Response(serializer.data)

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
def get_organization_list(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    objects = Organization.objects.filter(order_stage = 1,employee = auth_status['user_id'] ).all()
    serializer = SimpleOrganizationSerialzer(objects, many = True)
    return Response(serializer.data)

@api_view(['GET']) 
def get_organization(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    
    if("id" in request.headers):
        objects = Organization.objects.filter(id = request.headers["id"]).all()
        serializer = ComplexOrganizationSerialzer(objects, many = True)
        return Response(serializer.data)
    else:
        return Response({'status':'failed','message': 'organization id not passed'})
    

@api_view(['GET']) 
def download_organization_image(request):
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        print(auth_status)
        return Response(auth_status,401)
    if("id" in request.headers):
        objects = Organization.objects.filter(id =  request.headers["id"])
        serializer = OrganizationImageSerializer(objects.first())
        return Response(serializer.data)
    else:
        return Response({'status':'failed','message': 'organization id not passed'})

import datetime
from datetime import date
from django.db.models import Count, F, Value
from app_settings.models import ProjectSetting

@api_view(['GET']) 
def get_organizations_for_visit(request):
    settings = ProjectSetting.objects.first()
    days_before_contract = settings.days_before_contract
    from_date = date.today() - datetime.timedelta(days=360)
    to_date = date.today() + datetime.timedelta(days=days_before_contract)
    # delta = to_date - from_date
    # print(f'Difference is {delta.days} days')
    
    auth_status = JWTAuthentication.authenticate(request)
    if auth_status['status'] != 'succeed':
        return Response(auth_status,401)
    manager_user = ServiceSection.objects.filter(section_manager = auth_status['user_id'])
    if manager_user.count()>0:
        objects = Organization.objects.filter( id__in = Subquery(OrganizationService.objects.filter(is_visited = 0, service_section__in = Subquery(manager_user.values('id'))).values('organization'))).filter(Q(order_status_id=1) | Q(order_status_id=2) & Q(expected_date__range=(from_date,to_date)))
        serializer = ComplexOrganizationSerialzer(objects, many = True)
        services = OrganizationService.objects.filter(is_visited = 0,service_section__in = Subquery(manager_user.values('id')))
        service_serializer =  OrganizationServiceSerialzer(services,many = True)
        return Response({"orgs":serializer.data,"authorized_services" : service_serializer.data })
    section_employees = ServiceSectionEmployee.objects.filter(employee = auth_status['user_id'])
    if section_employees.count()>0:
        objects = Organization.objects.filter(id__in = RawSQL("select organization_id from orgs_organizationservice where is_visited = 0 and ( service_section_id, service_type_id) in %s ",[list(section_employees.values_list("service_section","service_type"))])).filter(Q(order_status_id=1) | Q(order_status_id=2) & Q(expected_date__range=(from_date,to_date))) 
        serializer = ComplexOrganizationSerialzer(objects, many = True)
        services = OrganizationService.objects.raw("select * from orgs_organizationservice where is_visited = 0 and ( service_section_id, service_type_id) in %s ",[list(section_employees.values_list("service_section","service_type"))])
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
        return Response(serializer.data)
    return Response([])


# @api_view(['GET']) 
# def get_org_emps_all(request):
#     objects = OrganizationEmployee.objects.filter(organization= request.GET.get("org_id")).all()
#     serializer = OrganizationEmployeeSerialzer(objects, many = True)
#     return Response(serializer.data)

# @api_view(['GET']) 
# def get_org_service_all(request):
#     objects = OrganizationService.objects.filter(organization= request.GET.get("org_id")).all()
#     serializer = OrganizationServiceSerialzer(objects, many = True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_organization(request):
#     serializer = OrganizationSerialzer(data = request.data)
#     if serializer.is_valid():
#         org = serializer.save()
#         print("create organizations")
#         return Response({'status':'succeed', 'message': 'organization_created_successfully',"data":org.id})
#     else:
#         return Response({'status':'failed','errors': serializer.errors})

# @api_view(['POST'])
# def update_organization_by_engineer(request):
#     serializer = EngineerNoteSerialzer(data = request.data)
#     if serializer.is_valid():
#         data = serializer.validated_data
#         print(data.get("engineer_note"))
#         Organization.objects.filter(id = data.get("organization")).update(engineer_note = data.get("engineer_note"))
        
#         return Response({'status':'succeed', 'message':'organization_created_successfully'})
#     else:
#         print({'status':'failed','errors': serializer.errors})
#         return Response({'status':'failed','errors': serializer.errors})
