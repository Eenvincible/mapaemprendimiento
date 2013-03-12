# Create your views here.
from django.shortcuts import render_to_response
from me.models import CompanyType, Company

def index(request):
    data = {}
    data['types'] = CompanyType.objects.all().order_by('id')
    data['companies'] = Company.objects.all()
    return render_to_response("base.html", data)