from django.contrib import admin
from me.models import CompanyType, Company, Sector, Zone

admin.site.register(CompanyType)
admin.site.register(Company)
admin.site.register(Sector)
admin.site.register(Zone)