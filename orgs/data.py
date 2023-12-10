# python.exe .\manage.py shell

from orgs.models import OrganizationType,OrderStatus,EmployeeRole,ServiceType,ServiceSection
OrderStatus.objects.create(name='جديد')
OrderStatus.objects.create(name='تحديد تاريخ')
OrderStatus.objects.create(name='محتمل')

EmployeeRole.objects.create(name='مالك')
EmployeeRole.objects.create(name='موظف')
EmployeeRole.objects.create(name='مدير')



ServiceType.objects.create(name='تركيب')
ServiceType.objects.create(name='صيانة')
ServiceType.objects.create(name='اعطال')


ServiceSection.objects.create(name='امن')
ServiceSection.objects.create(name='مصاعد')


OrganizationType.objects.create(name='برج')
OrganizationType.objects.create(name='مركز تجاري')

