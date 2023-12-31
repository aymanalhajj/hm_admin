from django.contrib import admin
from .models import UserAccount,UserType

class UserAccountAdmin(admin.ModelAdmin):
    
    list_display = ("id",'first_name' ,'username' ,'type')
    list_filter = ("id",'first_name','second_name','third_name','fourth_name' ,'last_name','email', 'mobile' ,'username' ,'type')
    search_fields = ("id",'first_name','second_name','third_name','fourth_name' ,'last_name','email', 'mobile' ,'username' ,'type')
    exclude = ('second_name','third_name','fourth_name' ,'last_name','email','mobile' ,)


class UserTypeAdmin(admin.ModelAdmin):    
    list_display = ("id",'name',)
    list_filter =  ("id",'name')
    search_fields =  ("id",'name')


def _register(model, admin_class = None):
    admin.site.register(model,admin_class)

_register(UserAccount,UserAccountAdmin)
_register(UserType,UserTypeAdmin)