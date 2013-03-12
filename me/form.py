from django import forms
from me.models import Company, CompanyType, Sector, Zone


class CompanyForm(forms.Form):
    name = forms.CharField(label='Tu Nombre')
    email = forms.CharField(label='Email')
    companyname = forms.CharField(label='Nombre Emprendimiento')
    companytype = forms.ModelChoiceField(CompanyType.objects.all(),label='Tipo')
    sector = forms.ModelChoiceField(Sector.objects.all(), label='Sector')
    address = forms.CharField(label='Direccion')
    website = forms.CharField(label='Sitio Web')
    description = forms.CharField(widget=forms.Textarea(), label="Descripcion")
    twitter = forms.CharField(label='Twitter')
    zone = forms.ModelChoiceField(Zone.objects.all(), label="Provincia")
