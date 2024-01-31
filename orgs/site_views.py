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
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
from .forms import MapForm

def last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - datetime.timedelta(days=next_month.day)

@staff_member_required
def get_clients_map(request):
    context = {
    # "is_popup": False,
    # "site_header": None,
    # "is_nav_sidebar_enabled": True,
    # "has_permission": True,
    # "title": "My title",
    # "subtitle": None,
    # "site_url": None,
    "available_apps": ['orgs',"app_settings"]
    }
    if request.method == "POST":
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        order_stage = int(request.POST["order_stage"])
        from_dt = datetime.datetime.strptime(from_date,"%Y-%m-%d").date()
        to_dt = datetime.datetime.strptime(to_date,"%Y-%m-%d").date()
    else:
        from_date = date.today()
        from_date = from_date.replace(day=1)
        to_date = last_day_of_month(date.today())

        month = from_date.month
        if month<10:
            month='0'+str(month)

        from_dt = from_date
        to_dt = to_date
        
        from_date = str(from_date.year)+'-'+ month +'-01'
        to_date = str(to_date.year)+'-'+ month +'-'+str(to_date.day)
        order_stage= 0
        form = MapForm()
    data = GeoLocation.objects.filter(Q(created_date__range=(from_dt,to_dt)))
    

    if order_stage != 0:
        data = data.filter(organization_id__in = Subquery(Organization.objects.filter(order_stage_id=order_stage).values("id")))
    
    stages = OrderStage.objects.all()
    context['from_date'] = from_date
    context['to_date'] = to_date
    context['data'] = data
    context['stages'] = stages
    context['title'] = "خارطة الإنتشار"
    context['order_stage'] = int(order_stage)
    print(context)
    # context['form'] =form
    return render(request, 'admin/our-clients.html', context)

# @staff_member_required
# def statistics_view(request):
#     return render(request, "statistics.html", {})

import datetime
from datetime import date
from django.db.models import Subquery, OuterRef,Q

# @staff_member_required
def get_organization_for_visit_by_section(request, from_date=None,to_date=None):
    from_dt = datetime.datetime.strptime(from_date,"%d%m%Y").date()
    to_dt = datetime.datetime.strptime(to_date,"%d%m%Y").date()
    
    settings = ProjectSetting.objects.first()
    days_before_contract = settings.days_before_contract
    from_date = date.today() - datetime.timedelta(days=360)
    to_date = date.today() + datetime.timedelta(days=days_before_contract)

    status_list = ServiceSection.objects.all()
    status_dict = dict()
    for status in status_list:
        status_dict[status.id] = status.name

    # Organization.objects.filter(Q(order_status_id=1) | Q(order_status_id=2) & Q(expected_date__range=(from_date,to_date)))
    orgs = OrganizationService.objects.filter(is_visited = 0)\
        .filter(organization_id__in = Subquery(Organization.objects.filter(Q(order_status_id=1) | Q(order_status_id=2) & Q(expected_date__range=(from_date,to_date))).values("id")) )\
        .filter(Q(created_date__range=(from_dt,to_dt)))
    grouped_orgs = orgs.values("service_section").annotate(count =Count("id")).values("service_section","count").order_by("-service_section")

    orgs_dict = dict()
    for group in grouped_orgs:
        orgs_dict[status_dict[group["service_section"]]] = group["count"]
    
    return JsonResponse({
        "title":"title",
        "data": {
            "labels": list(orgs_dict.keys()),
            "datasets": [{
                "label": "عدد العملاء",
                "fill": True,
                # "backgroundColor": generate_color_palette(len(orgs_dict)),
                # "borderColor": generate_color_palette(len(orgs_dict)),
                "data": list(orgs_dict.values()),
            }]
        },

    })

@staff_member_required
def get_organization_visit_by_emp(request, from_date=None,to_date=None):
    from_dt = datetime.datetime.strptime(from_date,"%d%m%Y").date()
    to_dt = datetime.datetime.strptime(to_date,"%d%m%Y").date()

    status_list = UserAccount.objects.all()
    status_dict = dict()
    for status in status_list:
        status_dict[status.id] = status.first_name


    orgs = OrganizationVisit.objects\
        .filter(Q(created_date__range=(from_dt,to_dt)))
    grouped_orgs = orgs.values("visitor").annotate(count =Count("id")).values("visitor","count").order_by("-visitor")

    orgs_dict = dict()
    for group in grouped_orgs:
        orgs_dict[status_dict[group["visitor"]]] = group["count"]
    
    return JsonResponse({
        "title":"title",
        "data": {
            "labels": list(orgs_dict.keys()),
            "datasets": [{
                "label": "عدد العملاء",
                # "backgroundColor": generate_color_palette(len(orgs_dict)),
                # "borderColor": generate_color_palette(len(orgs_dict)),
                "data": list(orgs_dict.values()),
            }]
        },

    })



@staff_member_required
def get_organizations_by_section(request, from_date=None,to_date=None):
    from_dt = datetime.datetime.strptime(from_date,"%d%m%Y").date()
    to_dt = datetime.datetime.strptime(to_date,"%d%m%Y").date()

    status_list = ServiceSection.objects.all()
    status_dict = dict()
    for status in status_list:
        status_dict[status.id] = status.name


    orgs = OrganizationService.objects\
        .filter(Q(created_date__range=(from_dt,to_dt)))
    grouped_orgs = orgs.values("service_section").annotate(count =Count("id")).values("service_section","count").order_by("-service_section")

    orgs_dict = dict()
    for group in grouped_orgs:
        orgs_dict[status_dict[group["service_section"]]] = group["count"]
    
    return JsonResponse({
        "title":"title",
        "data": {
            "labels": list(orgs_dict.keys()),
            "datasets": [{
                "label": "عدد العملاء",
                # "backgroundColor": generate_color_palette(len(orgs_dict)),
                # "borderColor": generate_color_palette(len(orgs_dict)),
                "data": list(orgs_dict.values()),
            }]
        },

    })

@staff_member_required
def get_organizations_by_state(request, from_date=None,to_date=None):
    from_dt = datetime.datetime.strptime(from_date,"%d%m%Y").date()
    to_dt = datetime.datetime.strptime(to_date,"%d%m%Y").date()

    status_list = OrderStatus.objects.all()
    status_dict = dict()
    for status in status_list:
        status_dict[status.id] = status.name


    orgs = Organization.objects\
        .filter(Q(created_date__range=(from_dt,to_dt)))
    grouped_orgs = orgs.values("order_status").annotate(count =Count("id")).values("order_status","count").order_by("-order_status")

    orgs_dict = dict()
    for group in grouped_orgs:
        orgs_dict[status_dict[group["order_status"]]] = group["count"]
    
    return JsonResponse({
        "title":"title",
        "data": {
            "labels": list(orgs_dict.keys()),
            "datasets": [{
                "label": "عدد العملاء",
                # "backgroundColor": generate_color_palette(len(orgs_dict)),
                # "borderColor": generate_color_palette(len(orgs_dict)),
                "data": list(orgs_dict.values()),
            }]
        },

    })


@staff_member_required
def get_organizations_by_emp(request, from_date=None,to_date=None):
    from_dt = datetime.datetime.strptime(from_date,"%d%m%Y").date()
    to_dt = datetime.datetime.strptime(to_date,"%d%m%Y").date()

    status_list = UserAccount.objects.all()
    status_dict = dict()
    for status in status_list:
        status_dict[status.id] = status.first_name


    orgs = Organization.objects\
        .filter(Q(created_date__range=(from_dt,to_dt)))
    grouped_orgs = orgs.values("employee").annotate(count =Count("id")).values("employee","count")

    orgs_dict = dict()
    for group in grouped_orgs:
        orgs_dict[status_dict[group["employee"]]] = group["count"]
    
    return JsonResponse({
        "title":"title",
        "data": {
            "labels": list(orgs_dict.keys()),
            "datasets": [{
                "label": "عدد العملاء",
                # "backgroundColor": generate_color_palette(len(orgs_dict)),
                # "borderColor": generate_color_palette(len(orgs_dict)),
                "data": list(orgs_dict.values()),
            }]
        },

    })

