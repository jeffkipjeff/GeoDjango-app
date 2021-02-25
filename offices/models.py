from django.contrib.gis.db import models


class FieldOffice(models.Model):
    number_of_staff = models.IntegerField()
    location = models.PointField()
    tag = models.CharField(max_length=200)


class RegionalOffice(models.Model):
    number_of_staff = models.IntegerField()
    location = models.PointField()
    tag = models.CharField(max_length=200)


class Issues(models.Model):
    issue = models.TextField()
    description = models.TextField()
    field_office = models.ForeignKey(FieldOffice, default=1, on_delete=models.SET_DEFAULT)
    regional_office = models.ForeignKey(RegionalOffice, default=1, on_delete=models.SET_DEFAULT)


class HeadOffice(models.Model):
    number_of_staff = models.IntegerField()
    location = models.PointField()
    tag = models.CharField(max_length=200)



