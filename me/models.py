from django.db import models

# Create your models here.
class CompanyType(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Compannia"
        verbose_name_plural = "Tipos de Compannia"

    def count_published(self, z):
        return self.company_set.filter(publish=True, zone=z).count()

class Sector(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"

class Zone(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"


class Company(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    companyname = models.CharField(max_length=200)
    type = models.ForeignKey(CompanyType)
    sector = models.ForeignKey(Sector)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    twitter = models.CharField(max_length=200, null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    zone = models.ForeignKey(Zone)
    publish = models.BooleanField()

    def __unicode__(self):
        return self.companyname

    class Meta:
        verbose_name = "Compannia"
        verbose_name_plural = "Compannias"

class Event(models.Model):
    organizer = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    eventname = models.CharField(max_length=200)
    starts = models.DateField()
    ends = models.DateField()
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    twitter = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
