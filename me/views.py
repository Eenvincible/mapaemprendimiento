# Create your views here.
import json
from django.db import transaction
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render_to_response
from me.form import CompanyForm
from me.models import CompanyType, Company, Zone


def type_repr(x, z):
    d = model_to_dict(x)
    d['count_published'] = x.count_published(z)
    return d

def index(request):
    data = {}
    data['zones'] = Zone.objects.all().order_by('-id')
    data['types'] = [type_repr(x,data['zones'][0]) for x in CompanyType.objects.all().exclude(id=4).order_by('id')]
    data['companies'] = Company.objects.filter(publish=True, zone=data['zones'][0])
    data['form'] = CompanyForm()

    return render_to_response("base.html", data)

def model_repr(x):
    d = model_to_dict(x, exclude=['name','zone','address'])
    d['sector'] = x.sector.name
    return d


@transaction.commit_manually
def places(request):
    try:
        zid = Zone.objects.get(pk=request.POST['zid'])
        data = {}
        data['companies'] = [model_repr(x) for x in Company.objects.filter(publish=True,zone=zid)]
        data['result'] = 'ok'
        data['lat'] = zid.lat
        data['lng'] = zid.lng
        data['types'] = {str(x.id): "%s (%s)"%(x.name, str(x.count_published(zid))) for x in CompanyType.objects.all().exclude(id=4).order_by('id')}
        transaction.commit()
        return HttpResponse(json.dumps(data), mimetype="application/json")
    except Exception as ex:
        transaction.rollback()
        return HttpResponse(json.dumps({"result":"bad", "error": str(ex)}),mimetype="application/json")

def post(request):
    try:
        c = Company(name = request.POST['name'],
                    email = request.POST['email'],
                    companyname = request.POST['companyname'],
                    type_id = request.POST['companytype'],
                    sector_id = request.POST['sector'],
                    address = request.POST['address'],
                    website = request.POST['website'],
                    description = request.POST['description'],
                    twitter = request.POST['twitter'],
                    lat = 0, lng = 0,
                    zone_id = request.POST['zone'],
                    publish = False)
        c.save()
        return HttpResponse(json.dumps({"result":"ok"}),mimetype="application/json")
    except:
        return HttpResponse(json.dumps({"result":"bad"}),mimetype="application/json")